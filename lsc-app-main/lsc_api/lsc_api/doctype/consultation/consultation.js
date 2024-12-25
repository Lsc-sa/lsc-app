frappe.ui.form.on('Consultation', {
    onload: function (frm) {
        // Initialize the fields with default values if empty
        if (!frm.doc.end_time) {
            frm.set_value('end_time', '12:00 AM');
        }
        if (!frm.doc.start_time) {
            frm.set_value('start_time', '12:00 AM');
        }
    },
    refresh: function (frm) {
        frappe.call({
            method: 'lsc_api.lsc_api.doctype.consultation.consultation.get_allowed_roles_from_settings',
            callback: function (response) {
                let allowed_roles = response.message || [];

                let has_permission = frappe.user_roles.some(role => allowed_roles.includes(role));
                console.log(allowed_roles);
                console.log(has_permission);

                if (!has_permission) {
                    $('.btn-comment').hide();
                    $('.comment-box').hide();
                    $('.custom-actions').hide();
                }
            }
        });


        frm.add_custom_button(__('Re Assign'), function () {
            let d = new frappe.ui.Dialog({
                title: 'Insert Employee',
                fields: [
                    {
                        label: 'Employee',
                        fieldname: 'employee',
                        fieldtype: 'Link',
                        options: "Employee",
                        reqd: 1
                    }
                ],
                primary_action_label: 'Set Employee',
                primary_action({ employee }) {
                    frappe.call({
                        method: 'set_employee',
                        doc: frm.doc,
                        args: {
                            employee
                        },
                        callback: function (response) {
                            console.log(response)
                            if (!response.exc) {
                                frm.reload_doc();
                            }
                        }
                    });
                    d.hide();
                }
            });

            d.show();
        });

        frm.add_custom_button(__('Add Link to Comments'), function () {
            let d = new frappe.ui.Dialog({
                title: 'Insert Link',
                fields: [
                    {
                        label: 'Use Fixed Link',
                        fieldname: 'use_custom_link',
                        fieldtype: 'Check',
                        description: 'Check to enter a custom link',
                        reqd: 0
                    },
                    {
                        label: 'Label',
                        fieldname: 'label',
                        fieldtype: 'Data',
                        description: 'Insert label (e.g., here is the meeting link!)',
                        reqd: 0
                    },
                    {
                        label: 'Link',
                        fieldname: 'link',
                        fieldtype: 'Small Text',
                        description: 'Insert link (e.g., http://meet.google.com)',
                        reqd: 0,
                        depends_on: 'eval: doc.use_custom_link == 0'
                    },
                    {
                        label: 'Fixed Link',
                        fieldname: 'custom_link',
                        fieldtype: 'Link',
                        options: 'Fixed Comment Links',
                        description: 'Select a predefined link..',
                        depends_on: 'eval: doc.use_custom_link == 1',
                        reqd: 0
                    },
                    {
                        label: 'New tab?',
                        fieldname: 'new_tab',
                        fieldtype: 'Check',
                        reqd: 0
                    },
                ],
                primary_action_label: 'Insert',
                primary_action(values) {
                    let comment;

                    if (values.use_custom_link) {
                        if (values.use_custom_link && values.custom_link) {
                            frappe.call({
                                method: 'frappe.client.get',
                                args: {
                                    doctype: 'Fixed Comment Links',
                                    name: values.custom_link
                                },
                                callback: function (r) {
                                    if (r.message) {
                                        let custom_link_value = r.message.link;

                                        comment = `label:${values.label} || tab: ${values.new_tab} || link:${custom_link_value}`;
                                        frappe.call({
                                            method: 'frappe.client.insert',
                                            args: {
                                                doc: {
                                                    doctype: 'Comment',
                                                    comment_type: 'Comment',
                                                    reference_doctype: frm.doctype,
                                                    reference_name: frm.docname,
                                                    content: comment
                                                }
                                            },
                                            callback: function (response) {
                                                if (!response.exc) {
                                                    frm.reload_doc();
                                                }
                                            }
                                        });
                                        d.hide();
                                    }
                                }
                            });
                        }
                    } else {
                        comment = `label:${values.label} || tab: ${values.new_tab} || link:${values.link}`;
                        frappe.call({
                            method: 'frappe.client.insert',
                            args: {
                                doc: {
                                    doctype: 'Comment',
                                    comment_type: 'Comment',
                                    reference_doctype: frm.doctype,
                                    reference_name: frm.docname,
                                    content: comment
                                }
                            },
                            callback: function (response) {
                                if (!response.exc) {
                                    frm.reload_doc();
                                }
                            }
                        });
                        d.hide();
                    }
                }
            });

            d.show();
        });

    }
});
