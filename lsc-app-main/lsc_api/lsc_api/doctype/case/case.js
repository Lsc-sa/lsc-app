frappe.ui.form.on("Case", {
  onload: function (listview) {
    // Add a custom button to the list view to show unarchived cases

    // By default, apply the filter to show only unarchived cases
    listview.filter_area.add([
      [listview.doctype, "archive_status", "!=", "Archived"],
    ]);
    listview.refresh();
  },
  // after_save: function (frm) {
  //     if (frm.doc.client_transaction) {
  //         frappe.call({
  //             method: 'sync_case_comments_to_client_transaction',
  //             frm: frm.doc,
  //             callback: function (response) {
  //                 if (response.message) {
  //                     // Update the last synced time
  //                     frappe.model.set_value(frm.doctype, frm.docname, "last_synced_comment_time", response.message);
  //                 }
  //             }
  //         });
  //     }
  // },

  refresh: function (frm) {
    frappe.call({
      method:
        "lsc_api.lsc_api.doctype.case.case.get_allowed_roles_from_settings",
      callback: function (response) {
        let allowed_roles = response.message || [];

        let has_permission = frappe.user_roles.some((role) =>
          allowed_roles.includes(role)
        );
        // console.log(allowed_roles);
        // console.log(has_permission);
        if (!has_permission) {
          $(".btn-comment").hide();
          $(".comment-box").hide();
          $(".custom-actions").hide();
        }
      },
    });

    frm.add_custom_button(__("Add Link to Comments"), function () {
      let d = new frappe.ui.Dialog({
        title: "Insert Link",
        fields: [
          {
            label: "Use Fixed Link",
            fieldname: "use_custom_link",
            fieldtype: "Check",
            description: "Check to enter a custom link",
            reqd: 0,
          },
          {
            label: "Label",
            fieldname: "label",
            fieldtype: "Data",
            description: "Insert label (e.g., here is the meeting link!)",
            reqd: 0,
          },
          {
            label: "Link",
            fieldname: "link",
            fieldtype: "Small Text",
            description: "Insert link (e.g., http://meet.google.com)",
            reqd: 0,
            depends_on: "eval: doc.use_custom_link == 0",
          },
          {
            label: "Fixed Link",
            fieldname: "custom_link",
            fieldtype: "Link",
            options: "Fixed Comment Links",
            description: "Select a predefined link..",
            depends_on: "eval: doc.use_custom_link == 1",
            reqd: 0,
          },
          {
            label: "New tab?",
            fieldname: "new_tab",
            fieldtype: "Check",
            reqd: 0,
          },
        ],
        primary_action_label: "Insert",
        primary_action(values) {
          let comment;

          if (values.use_custom_link) {
            if (values.use_custom_link && values.custom_link) {
              frappe.call({
                method: "frappe.client.get",
                args: {
                  doctype: "Fixed Comment Links",
                  name: values.custom_link,
                },
                callback: function (r) {
                  if (r.message) {
                    let custom_link_value = r.message.link;

                    comment = `label:${values.label} || tab: ${values.new_tab} || link:${custom_link_value}`;
                    frappe.call({
                      method: "frappe.client.insert",
                      args: {
                        doc: {
                          doctype: "Comment",
                          comment_type: "Comment",
                          reference_doctype: frm.doctype,
                          reference_name: frm.docname,
                          content: comment,
                        },
                      },
                      callback: function (response) {
                        if (!response.exc) {
                          frm.reload_doc();
                        }
                      },
                    });
                    d.hide();
                  }
                },
              });
            }
          } else {
            comment = `label:${values.label} || tab: ${values.new_tab} || link:${values.link}`;
            frappe.call({
              method: "frappe.client.insert",
              args: {
                doc: {
                  doctype: "Comment",
                  comment_type: "Comment",
                  reference_doctype: frm.doctype,
                  reference_name: frm.docname,
                  content: comment,
                },
              },
              callback: function (response) {
                if (!response.exc) {
                  frm.reload_doc();
                }
              },
            });
            d.hide();
          }
        },
      });

      d.show();
    });

    // Check the current status and show/hide buttons accordingly
    if (frm.doc.archive_status === "Archived") {
      frm.remove_custom_button(__("Archive"));
      frm.add_custom_button(__("Unarchive"), function () {
        frappe.confirm(
          "Are you sure you want to unarchive this document?",
          function () {
            frappe.call({
              method: "frappe.client.set_value",
              args: {
                doctype: "Cases",
                name: frm.doc.name,
                fieldname: "archive_status",
                value: "", // Change this to the original or desired status
              },
              callback: function (response) {
                if (!response.exc) {
                  frappe.msgprint(
                    "This document has been unarchived successfully."
                  );
                  frm.reload_doc();
                } else {
                  frappe.msgprint(
                    "There was an issue unarchiving this document."
                  );
                }
              },
            });
          },
          function () {
            frappe.msgprint("Action cancelled.");
          }
        );
      });
    } else {
      frm.remove_custom_button(__("Unarchive"));
      frm.add_custom_button(__("Archive"), function () {
        frappe.confirm(
          "Are you sure you want to archive this document?",
          function () {
            frappe.call({
              method: "frappe.client.set_value",
              args: {
                doctype: "Case",
                name: frm.doc.name,
                fieldname: "archive_status",
                value: "Archived",
              },
              callback: function (response) {
                if (!response.exc) {
                  frappe.msgprint(
                    "This document has been archived successfully."
                  );
                  frm.reload_doc();
                } else {
                  frappe.msgprint(
                    "There was an issue archiving this document."
                  );
                }
              },
            });
          },
          function () {
            frappe.msgprint("Action cancelled.");
          }
        );
      });
    }
  },
  // Attach event listener to the button
  archive: function (frm) {
    // Update the checkbox field value to "1" (checked)
    var checkbox_value = frm.doc.archived;

    // Toggle the checkbox value between 0 (unchecked) and 1 (checked)
    frm.set_value("archived", checkbox_value ? 0 : 1);

    // Trigger a save operation to persist the changes
    frm.save();

    // Define translated messages
    var archived_message = __("The case has been Archived");
    var cancelled_message = __("The case has been UnArchived");

    if (frm.doc.archived == 1) {
      frappe.show_alert({
        message: archived_message,
        indicator: "green",
      });
    } else if (frm.doc.archived == 0) {
      frappe.show_alert({
        message: cancelled_message,
        indicator: "blue",
      });
    }
  },
});
