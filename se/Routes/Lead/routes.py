from se.Controllers.Controller.LeadController import LeadController
from se.Controllers.BaseController import BaseController
from flask import Flask , Blueprint , request ,jsonify
from se.Transformer.LeadTransformer import transform
from se.Exceptions.SeException import SeException

app = Flask(__name__)
lead = Blueprint('lead' , __name__ , url_prefix='/lead management')


@lead.route('/mail' , methods =['POST'])
def store():
	result = LeadController().store(request)
	if result:
		return transform(result)
	
@lead.route('/<leadId>', methods=['GET'])
def getLeadById(leadId):
	result = LeadController().get_lead_by_id(leadId)
	if result:
		return transform(result)
@lead.route('/<leadId>', methods=['DELETE'])
def deleteLeadById(leadId):
	result = LeadController().delete_lead_by_id(leadId)
	return BaseController().respond(200, [])

@lead.route('/upload attachment' , methods =['POST'])
def uploadAttachment():
	result = LeadController().upload_attachment(request)
	return result

@lead.errorhandler(404)
def NotFoundException(error):
	exception = SeException(404, 'SE_404_AWS', 'Not found', 'check your request')
	return exception.throw_se_exception()

@lead.errorhandler(400)
def BadRequestException(error):
	exception = SeException(400, 'SE_400_AWS', 'Bad Request', 'check your request')
	return exception.throw_se_exception()

@lead.errorhandler(500)
def InternalServerError(error):
	exception = SeException(400, 'SE_400_AWS', 'Bad Request', 'check your request')
	return exception.throw_se_exception()
@lead.errorhandler(SeException)
def customException(error):
    return error.throw_se_exception()