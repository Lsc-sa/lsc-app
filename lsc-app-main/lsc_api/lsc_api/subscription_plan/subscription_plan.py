import frappe
from frappe import _
import requests
from requests.auth import HTTPBasicAuth
from lsc_api.utils.error_handler import handle_error
from lsc_api.utils.jwt import verify_jwt_middleware
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse


@frappe.whitelist(methods=["GET"])
def get_subscription_status():
    # Get the current authenticated user
    user = frappe.session.user
    account_spage = frappe.get_all("Account Status Page", {"user": user}, "*")
    account_status = frappe.db.get_value(
        "Account Status Page", {"user": user}, "status"
    )

    # Get customer
    customer = frappe.get_list(
        "Customer", filters={"custom_user": user}, limit=1, fields=["name"]
    )
    if not customer:
        return {"data": {"message": "This user has no customer doc"}}

    customer = customer[0]
    subscription_id = frappe.db.exists(
        "Subscription", {"status": "Active", "party": customer.name}
    )

    if subscription_id:
        subscription = frappe.get_doc(
            "Subscription", {"name": subscription_id, "status": "Active"}
        )
        subscription_plan_id = subscription.plans[0]

        subscription_plan = frappe.get_doc(
            "Subscription Plan", subscription_plan_id.plan
        )

        quota = frappe.get_all(
            "Quota", {"parent": subscription_id, "parentfield": "custom_quota"}, "*"
        )

        remaining_cons = 0
        remaining_cases = 0
        remaining_legals = 0

        for row in quota:
            if row.service_name == "ساعات الاستشارة":
                remaining_cons = row.hrs
            elif row.service_name == "ساعات الخدمات القانونية":
                remaining_legals = row.hrs
            elif row.service_name == "ساعات القضايا":
                remaining_cases = row.hrs

        # return subscription_plan
        total_hours = (
            int(subscription_plan.custom_total_hrs)
            + int(subscription_plan.custom_total_hrs_cases)
            + int(subscription_plan.custom_total_hrs_legal_services)
        )

        allowed_services = [
            _(r.service_name) for r in subscription_plan.custom_allowed_services
        ]
        remaining_hours = 0
        for r in subscription.custom_quota:
            remaining_hours += int(r.hrs)

        return {
            "data": {
                "subscription": {
                    "subscription_plan": _(subscription_plan.name),
                    "plan_fees": subscription_plan.cost,
                    "status": _(subscription.status),
                    "invoice_start_date": subscription.current_invoice_start,
                    "invoice_end_date": subscription.current_invoice_end,
                    "consultation_hrs": subscription_plan.custom_total_hrs,
                    "remaining_consultation_hrs": remaining_cons,
                    "cases_hrs": subscription_plan.custom_total_hrs_cases,
                    "remaining_cases_hrs": remaining_cases,
                    "legal_services_hrs": subscription_plan.custom_total_hrs_legal_services,
                    "remaining_legal_services_hrs": remaining_legals,
                    "total_hours": total_hours,
                    "remaining_hours": remaining_hours,
                    "allowed_services": allowed_services,
                }
            },
            "asp_status": account_status,
        }

    return {"data": {"subscription": None}, "asp_status": account_status}


@frappe.whitelist(methods=["GET"])
def get_subscriptions():
    user = frappe.session.user
    user_language = frappe.db.get_value("User", {"name": user}, "language")
    account_spage = frappe.get_all("Account Status Page", {"user": user}, "*")
    account_status = frappe.db.get_value(
        "Account Status Page", {"user": user}, "status"
    )
    try:
        params = frappe.local.request.args
        # Convert parameters to integers
        try:
            page = params.get("page")
            size = params.get("size")

            page = int(page) if page else 1
            size = int(size) if size else 5
        except ValueError:
            return handle_error("Page number and page length should be integers")

        limit_start = (page - 1) * size

        # Fetch the list of subscription plans with their allowed services
        plans = frappe.get_all(
            "Subscription Plan",
            {"disabled": 0},
            "*",
            order_by="cost desc",
            # limit_start=limit_start,
            # limit_page_length=size,
        )

        # For each plan, fetch the associated allowed services
        for plan in plans:
            plan["plan_name"] = _(plan["plan_name"])
            plan["currency"] = _(plan["currency"])
            plan["billing_interval"] = _(plan["billing_interval"])

            plan_items = frappe.get_all(
                "Allowed Service",
                fields=["service_name"],
                filters={"parent": plan["name"]},
            )
            for item in plan_items:
                item["service_name"] = _(item["service_name"])
            plan["allowed_services"] = plan_items

            if user_language == "en":
                plan["plan_requiries"] = plan["custom_plan_requiries_in_english"]
            else:
                plan["plan_requiries"] = plan["custom_plan_requiries"]

        return {
            "message": "success",
            "length": len(plans),
            "data": plans,
            "asp_status": account_status,
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error fetching subscription plans"))
        return {"error": str(e)}


@frappe.whitelist(allow_guest=True, methods=["POST"])
def create_subscription(**kwargs):
    try:
        # Get the current authenticated user
        user = frappe.session.user

        data = kwargs.get("data")
        plan_name = data.get("plan_name")

        # Validate the input parameters (plan_name, start_date, end_date)
        if not plan_name:
            return {"status": "error", "message": _("plan_name field is required.")}

        # Fetch the Subscription Plan to ensure it exists
        plan = frappe.get_doc("Subscription Plan", plan_name)
        if not plan:
            return {"error": _("The subscription plan does not exist.")}

        # Get customer
        customer = frappe.get_list("Customer", filters={"custom_user": user}, limit=1)
        if not customer:
            return {"status": "fail", "message": _("This user has no customer.")}

        customer = customer[0]

        # subscription_id = frappe.db.exists("Subscription", {"status": "Unpaid", "party": customer.name})
        # if subscription_id:
        #     if frappe.db.exists("Subscription Plan Detail", {"parent":subscription_id, "plan": plan.name }):
        #         subscription = frappe.get_doc("Subscription", {"status": "Unpaid", "party": customer.name})

        #         return {
        #             "status": "success",
        #             "message": _("Subscription is already created successfully, Complete the payment process."),
        #             "data": {
        #                 "sales_invoice": subscription.custom_sales_invoice
        #             },
        #         }

        # Create the Subscription entry
        subscription = frappe.get_doc(
            {
                "doctype": "Subscription",
                "party_type": "Customer",
                "party": customer.name,
                "company": "LSC",
                "status": "Unpaid",
                "days_until_due": 5,
                "generate_invoice_at": "Beginning of the current subscription period",
                "generate_new_invoices_past_due_date": 1,
                "submit_invoice": 1,
                "sales_tax_template": "KSA VAT 15% - LSC",
                # "start_date": start_date, # paid day
                # "end_date": end_date, # paid day plus based on the interval of subscription plan
            }
        )

        # Add child table plans {plan, qty}
        subscription.append(
            "plans",
            {
                "plan": plan.name,
                "qty": 1,
            },
        )

        subscription.insert(ignore_permissions=True)
        subscription.status = "Unpaid"
        subscription.save(ignore_permissions=True)

        if frappe.db.exists("Sales Invoice", subscription.custom_sales_invoice):
            sales_inv = frappe.get_doc(
                "Sales Invoice", subscription.custom_sales_invoice
            )
        else:
            return {
                "status": "fail",
                "message": _("Subscription created but cannot find invoice."),
            }

        return {
            "status": "success",
            "message": _("Subscription created successfully."),
            "data": {"sales_invoice": sales_inv.name},
        }

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Error creating subscription"))
        return {"error": str(e)}


@frappe.whitelist(methods=["POST"])
def pay_subscription(**kwargs):
    base_host = frappe.request.host
    try:
        payment_settings = frappe.get_doc("Payment Settings")
        secret_key = None
        if payment_settings.use_live:
            secret_key = payment_settings.live_secret_key
        else:
            secret_key = payment_settings.test_secret_key

        # Get the current authenticated user
        user = frappe.session.user
        user_lang = frappe.db.get_value("User", user, "language")
        
        user_data = frappe.get_all(
            "User",
            filters={"name": user},
            fields=["first_name", "middle_name", "last_name", "phone"],
            limit=1,
        )
        if not user_data:
            return {"status": "fail", "message": "User not found"}
        user_data = user_data[0]

        # Extract data from kwargs
        data = kwargs.get("data")
        sales_invoice = data.get("sales_invoice")

        # Retrieve the invoice and customer details
        invoice = frappe.get_doc("Sales Invoice", sales_invoice)
        customer = frappe.get_doc("Customer", invoice.customer)

        if not sales_invoice:
            return {"status": "fail", "message": "Sales invoice not provided"}

        # Check if Sales Invoice exists
        if not frappe.db.exists("Sales Invoice", {"name": sales_invoice}):
            return {
                "status": "fail",
                "message": f"This sales invoice {sales_invoice} is not found",
            }

        if frappe.db.exists("Sales Invoice", {"name": sales_invoice, "status": "Paid"}):
            return {
                "status": "fail",
                "message": f"This sales invoice {sales_invoice} is already Paid",
            }

        try:
            # Fetch the Subscription linked to the sales invoice
            subscription = frappe.get_doc(
                "Subscription", {"custom_sales_invoice": sales_invoice}
            )

            # Get the subscription plan details
            subscription_plan = frappe.get_all(
                "Subscription Plan",
                filters={"name": subscription.plans[0].plan},
                fields=["cost", "name", "currency"],
                limit=1,
            )
            if not subscription_plan:
                return {"status": "fail", "message": "Subscription plan not found"}
            subscription_plan = subscription_plan[0]

            # Payment API request
            url = "https://api.moyasar.com/v1/invoices"
            headers = {
                "Content-Type": "application/json",
            }

            # payer_ip = (
            #     frappe.local.request.headers.get("X-Forwarded-For")
            #     or frappe.local.request.remote_addr
            # )

            # Prepare payment data
            payment_data = {
                "description": subscription_plan.name,
                "amount": int(subscription_plan.cost * 100),
                "currency": subscription_plan.currency,
                # "fee": "0",
                # "refunded": "0",
                # "captured": "0",
                # "ip": payer_ip,
                "metadata": {
                    "user": user,
                    "sales_invoice": sales_invoice,
                    "custom_status": "pending_payment",
                    "customer": {
                        "first_name": user_data.get("first_name"),
                        "middle_name": user_data.get(
                            "middle_name", user_data.get("first_name")
                        ),
                        "last_name": user_data.get("last_name"),
                        "email": user,
                        "phone": {"number": user_data.get("phone")},
                    },
                },
                # "source": {"id": "src_all"},  # Allow all sources
                "callback_url": f"https://{base_host}/api/method/lsc_api.lsc_api.subscription_plan.subscription_plan.tap_handler",
                "success_url": f"https://{base_host}/dashboard/profile/payRes",
            }

            try:
                # Make the payment request
                response = requests.post(
                    url,
                    headers=headers,
                    json=payment_data,
                    auth=(secret_key, ""),
                )

                # response.raise_for_status()  # Raise exception for HTTP errors
                response_data = response.json()
                if user_lang == "ar":
                    response_data["url"] = modify_lang_in_url(response_data["url"], user_lang)

                # Update the subscription with the tap charge ID
                subscription.custom_tap_charge_id = response_data["id"]
                subscription.save(ignore_permissions=True)
                return {
                    "status": "success",
                    "response": response_data,
                    "CALLER": "OMAR",
                    "data": {"transaction": response_data["url"]},
                }
            except:
                return {
                    "status": "fail",
                    "response": response_data,
                    "message": "Fail to create checkout url",
                }

        except requests.exceptions.RequestException as e:
            return {"status": "fail", "message": f"Payment API error: {str(e)}"}
        except frappe.DoesNotExistError:
            return {"status": "fail", "message": "Subscription not found"}
        except Exception as e:
            frappe.log_error(frappe.get_traceback(), _("Payment FAILED"))
            return {
                "status": "fail",
                "message": "Something is wrong",
            }

    except frappe.DoesNotExistError:
        return {"status": "fail", "message": "User not found"}
    except Exception as e:
        return {"status": "fail", "message": f"An unexpected error occurred: {str(e)}"}


@frappe.whitelist(allow_guest=True)
def tap_handler(**kwargs):
    base_host = frappe.request.host
    try:
        frappe.set_user("Administrator")
        data = frappe.request.json
        frappe.log_error(frappe.as_json(data), "Moyasar Webhook Response")
        payment_status = data.get("status")
        payment_id = data.get("payments")[0].get("id")

        sales_invoice_name = data.get("metadata").get("sales_invoice")

        if not sales_invoice_name:
            frappe.log_error("No reference ID found in Moyasar webhook data")
            return

        # transaction = data.get("transaction", {})
        transaction_amount = data.get("amount")
        transaction_amount = float(transaction_amount / 100)
        if not transaction_amount:
            frappe.log_error(transaction_amount, "Transaction amount is missing")
            return

        if payment_status == "paid":
            try:
                sales_invoice = frappe.get_doc("Sales Invoice", sales_invoice_name)
            except frappe.DoesNotExistError:
                frappe.log_error(f"Sales Invoice {sales_invoice_name} does not exist")
                return
            company_settings = frappe.get_doc("Company", "LSC")
            payment_entry_data = {
                "doctype": "Payment Entry",
                "payment_type": "Receive",
                "party_type": "Customer",
                "party": sales_invoice.customer,
                "posting_date": frappe.utils.nowdate(),
                "mode_of_payment": "نقد",  # Set to the appropriate mode of payment
                "paid_from": company_settings.default_receivable_account,
                "paid_to": company_settings.default_cash_account,
                "paid_amount": transaction_amount,
                "received_amount": transaction_amount,
                "references": [
                    {
                        "reference_doctype": "Sales Invoice",
                        "reference_name": sales_invoice.name,
                        "allocated_amount": transaction_amount,
                        "account": company_settings.default_receivable_account,
                    }
                ],
                "remarks": f"Payment against Sales Invoice: {sales_invoice.name}",
            }

            payment_entry = frappe.get_doc(payment_entry_data)
            payment_entry.insert(ignore_permissions=True)
            payment_entry.submit()

            # Set subscription to active if applicable
            subscription = frappe.get_doc(
                "Subscription", {"custom_sales_invoice": sales_invoice.name}
            )
            subscription.status = "Active"
            subscription.custom_moyasar_payment_id = payment_id
            subscription.save(ignore_permissions=True)

            subscription_plan_id = subscription.plans[0]

            subscription_plan = frappe.get_doc(
                "Subscription Plan", subscription_plan_id.plan
            )

            #  Cancel previous subscriptions
            customer_subscriptions = frappe.get_all(
                "Subscription",
                filters={
                    "party": sales_invoice.customer,
                    "status": "Active",
                    "name": ["!=", subscription.name],
                },
                fields=["name"],
            )

            for subscription in customer_subscriptions:
                old_subscription = frappe.get_doc(
                    "Subscription", subscription.get("name")
                )
                old_subscription.status = "Cancelled"
                old_subscription.save(ignore_permissions=True)

            # Cancel previous contracts
            customer_contracts = frappe.get_all(
                "Contract",
                filters={
                    "party_name": sales_invoice.customer,
                },
                fields=["name"],
            )

            for contract in customer_contracts:
                frappe.db.set_value(
                    "Contract", {"name": contract["name"]}, "status", "Inactive"
                )
            frappe.db.commit()

            user = data.get("metadata").get("user")
            account_spage = frappe.get_doc("Account Status Page", {"user": user})
            account_spage.contract_status = None
            account_spage.status = "Incomplete"
            account_spage.save(ignore_permissions=True)

            contract_template = frappe.get_all(
                "Contract Template",
                fields="name, contract_terms, custom_company_signature",
            )
            frappe.set_user(user)

            if contract_template:
                contract_data = dict(contract_template[0])

                new_contract = frappe.get_doc(
                    {
                        "doctype": "Contract",
                        "party_type": "Customer",
                        "party_user": user,
                        "party_name": sales_invoice.customer,
                        "custom_subscription_plan": subscription_plan.name,
                        "custom_subscription": subscription.name,
                        "start_date": subscription.current_invoice_start,
                        "end_date": subscription.current_invoice_end,
                        "contract_template": contract_data["name"],
                        "contract_terms": contract_data["contract_terms"],
                        "signee_company": contract_data["custom_company_signature"],
                    }
                )

                new_contract.insert(ignore_permissions=True)
                new_contract.submit()
                # frappe.log_error(str(user))

                frappe.set_value(
                    "Account Status Page",
                    {"name": account_spage.name},
                    "contract",
                    new_contract.name,
                )
                frappe.db.commit()

            else:
                frappe.throw("No contract template found.")

            return {
                "status": "success",
                "redirect": f"https//{base_host}/success",
            }
        elif payment_status == "canceled":
            frappe.log_error(f"Payment failed for Sales Invoice {sales_invoice_name}")
            return {"status": "fail", "redirect": f"https//{base_host}/failure"}
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), _("Payment Initiation Failed"))
        return {"status": "error", "redirect": f"https//{base_host}/failure"}


def modify_lang_in_url(url, user_lang):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    if user_lang == "ar":
        query_params["lang"] = "ar"
    else:
        query_params.setdefault("lang", "en")  

    new_query = urlencode(query_params, doseq=True)
    modified_url = urlunparse(
        (parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, new_query, parsed_url.fragment)
    )
    return modified_url