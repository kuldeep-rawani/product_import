from se.Repositories.Mailer.LeadRepository import LeadRepository
from se.Repositories.Mailer.UploadRepository import UploadRepository
from se.Wrapper.Wrapper import wrapper_class
from flask_mail import Mail, Message
from flask import Flask

class LeadController:

	mailerUrl = "http://127.0.0.1:5000/mail/"
	uploadUrl = "http://127.0.0.1:5000/upload"

	def store(self, request):
		wrappedObject = wrapper_class().wrapper(request)
		return LeadRepository(self.mailerUrl).store(wrappedObject)

	def get_lead_by_id(self, leadId):
		return LeadRepository(self.mailerUrl).get_lead_by_id(leadId)

	def delete_lead_by_id(self, leadId):
		return LeadRepository(self.mailerUrl).delete_lead_by_id(leadId)
	

	def upload_attachment(self, request):
		return UploadRepository(self.uploadUrl).upload_attachment(request)

		
	    	