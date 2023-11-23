// Copyright (c) 2023, Montego-arch and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Member', {
	// Add CUSTOM Button
	refresh: function(frm) {
		frm.add_custom_button("Button One", function () {
			let fName = frm.doc.first_name;
			let lName = frm.doc.last_name;
			frm.set_value("full_name", fName + " " + lName)
			frappe.msgprint(email);
		},'Action'),
		frm.add_custom_button("Button Two", function () {
			frappe.call({
				method:
					"library_management.library_management.doctype.library_member.api.get_all_members",
				callback: function (r) {
					console.log(r);
				},
			});
		},'Action'),
		frm.add_custom_button(
			"Button Three",
			function () {
				frappe.prompt("Phone Number", ({ value }) => {
					if (value) {
						frm.set_value("phone", value);
						frm.refresh_field("phone");
						frappe.msgprint("Phone number added successfully.");
					}
				});
			},
			"Action"
		);
	},
});
