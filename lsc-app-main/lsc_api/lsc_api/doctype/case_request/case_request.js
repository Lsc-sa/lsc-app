frappe.ui.form.on("Case Request", {
    refresh: function(frm) {
        if (frm.doc.case_title) {
            fetch_and_display_claim_parties(frm);
        }
    },
    case_title: function(frm) {
        if (frm.doc.case_title) {
            fetch_and_display_claim_parties(frm);
        }
    }
});

function fetch_and_display_claim_parties(frm) {
    console.log("Fetching claim parties for case reference:", frm.doc.case_title);

    frappe.call({
        method: 'frappe.client.get',
        args: {
            doctype: 'Cases',
            name: frm.doc.case_title
        },
        callback: function(r) {
            if (r.message) {
                let case_doc = r.message;
                //console.log("Case document fetched:", case_doc);

                let claim_parties = case_doc.claim_parties;
                //console.log("Claim parties:", claim_parties);
                var ClaimParties = __('Claim Party');
                var ClaimName = __('Name');
                var ClaimID = __('ID Number/Passport');
                var ClaimNationality = __('Nationality');
                var ClaimPartyType = __('Party type');
                if (claim_parties && claim_parties.length > 0) {
                    let html = '<table class="table table-bordered">';
                    html += ClaimParties+'<thead><tr><th>'+ClaimName+'</th><th>'+ClaimID+'</th><th>'+ClaimNationality+'</th><th>'+ClaimPartyType+'</th></tr></thead>';
                    html += '<tbody>';
                    claim_parties.forEach(function(party) {
                        html += `<tr><td>${party.claim_name}</td><td>${party.claim_id_number}</td><td>${party.nationality}</td><td>${party.party_type}</td></tr>`;
                    });
                    html += '</tbody></table>';
                    frm.get_field('claim_parties_preview').$wrapper.html(html);
                } else {
                    frm.get_field('claim_parties_preview').$wrapper.html('<p></p>');
                }
            } else {
                frm.get_field('claim_parties_preview').$wrapper.html('<p>No data found for the selected case reference</p>');
            }
        },
        error: function() {
            frm.get_field('claim_parties_preview').$wrapper.html('<p>Error fetching data</p>');
        }
    });
}
