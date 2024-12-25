frappe.ui.form.on('Case Sessions', {
    refresh: function (frm) {
        frm.add_custom_button(__('Re Assign'), function () {
            let d = new frappe.ui.Dialog({
                title: 'Insert Employee',
                fields: [
                    {
                        label: 'Employee',
                        fieldname: 'employee',
                        fieldtype: 'Link',
                        options:"Employee",
                        reqd: 1
                    }
                ],
                primary_action_label: 'Set Employee',
                primary_action({ employee }) {
                    frappe.call({
                        method: 'set_employee',
                        doc:frm.doc,
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


    }
});
