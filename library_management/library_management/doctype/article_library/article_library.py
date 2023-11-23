# Copyright (c) 2023, Montego-arch and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from library_management.utils import sendmail

class Article_Library(Document):

	def validate(self):
		if (self.track_buyers == 0):
			if (self.buyers):
				frappe.throw('This article does not track buyer.')


	def before_save(doc):
		message = f"A new article has been added to your account"
		sendmail(doc, ['john@gmail.com', 'testmail.com'], message, "New")
		# frappe.msgprint('Article saved and Email sent!')
