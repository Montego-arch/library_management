# Copyright (c) 2023, Montego-arch and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class LibraryMembership(Document):
	def before_save(self):
		if(self.library_member == "LM000001"):
			self.paid = 1
		else:
			self.paid = 0
