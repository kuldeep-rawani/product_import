from product_importer.controllers.product_controller import ProductController
from product_importer.controllers.base_controller import BaseController
from flask import Flask , Blueprint , request ,jsonify, render_template, make_response
from product_importer.exceptions.custom_exception import CustomException

app = Flask(__name__)
product = Blueprint('product' , __name__ , url_prefix='/products')

""" upload file """
@product.route('/import' , methods =['POST'])
def upload_products():
	result, response_msg = ProductController().upload_products(request)
	if not result:
		return make_response(jsonify([{'result': response_msg}]), 400)
	return jsonify([])

""" filter products """
@product.route('/', methods=['GET'])
def product_filter():
	result = ProductController().product_filter(request)
	if not result:
		return make_response(jsonify([{'result': 'No Products'}]), 400)
	return jsonify(result)

""" webhook url """
@product.route('/webhook', methods=['POST'])
def webhook():
	result = ProductController().webhook(request)
	if not result:
		return make_response(jsonify([{'result': 'No Products'}]), 400)
	return jsonify({'result': 'Product created notification'})


""" custom exceptions handinlg """
@product.errorhandler(404)
def NotFoundException(error):
	exception = CustomException(404, 'fulfil_io_404', 'Not found', 'check your request')
	return exception.throw_fulfil_exception()

@product.errorhandler(400)
def BadRequestException(error):
	exception = CustomException(400, 'fulfil_io_400', 'Bad Request', 'check your request')
	return exception.throw_fulfil_exception()

@product.errorhandler(500)
def InternalServerError(error):
	exception = CustomException(400, 'fulfil_io_400', 'Bad Request', 'check your request')
	return exception.throw_fulfil_exception()
@product.errorhandler(CustomException)
def customException(error):
    return error.throw_se_exception()