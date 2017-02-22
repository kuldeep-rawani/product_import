from flask import Flask, request

app = Flask(__name__)


class wrapper_class:

	def wrapper(self, request):
		dict = {}
		dict['body'] = request.form['body']
		dict['subject'] = request.form['subject']
		dict['sender'] = request.form['sender']
		dict['cc'] = request.form.getlist('cc')
		dict['bcc'] = request.form.getlist('bcc')
		dict['receiver'] = request.form.getlist('receiver')
		dict['attachments'] = request.files.getlist('files[]')
		dict['company'] = request.form['company']
		dict['country'] = request.form['country']
		dict['firstName'] = request.form['firstName']
		dict['lastName'] = request.form['lastName']
		dict['phone'] = request.form['phone']
		dict['projectType'] = request.form['projectType']
		dict['state'] = request.form['state']
		dict['signUpNewsLetter']  = request.form['signUpNewsLetter']
		dict['aboutProject'] = request.form['aboutProject']

		return dict
