import frappe

@frappe.whitelist()
def get_all_members():
    members = frappe.db.sql(f"""SELECT full_name, email_address FROM `tabLibrary Member`;""", as_dict=True)
    return members

@frappe.whitelist(allow_guest=True)
def get_member(member_id ):
    member_details = frappe.db.sql(f"""SELECT full_name, email_address FROM `tabLibrary Member` WHERE name='{member_id}';""", as_dict=True)

    if(member_details):
        return member_details
    else:
        return "Member does not exist"