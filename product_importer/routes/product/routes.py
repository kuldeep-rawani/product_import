from product_importer.controllers.product_controller import ProductController
from product_importer.controllers.base_controller import BaseController
from flask import Flask , Blueprint , request ,jsonify, render_template
from product_importer.exceptions.custom_exception import CustomException

app = Flask(__name__)
product = Blueprint('product' , __name__ , url_prefix='/products')


@product.route('/import' , methods =['POST'])
def upload_products():
	result = ProductController().upload_products(request)
	return jsonify([])
@product.route('/', methods=['GET'])
def product_filter():
	result = ProductController().product_filter(request)
	return jsonify(result)

@product.errorhandler(404)
def NotFoundException(error):
	exception = CustomException(404, 'SE_404_AWS', 'Not found', 'check your request')
	return exception.throw_se_exception()

@product.errorhandler(400)
def BadRequestException(error):
	exception = CustomException(400, 'SE_400_AWS', 'Bad Request', 'check your request')
	return exception.throw_se_exception()

@product.errorhandler(500)
def InternalServerError(error):
	exception = CustomException(400, 'SE_400_AWS', 'Bad Request', 'check your request')
	return exception.throw_se_exception()
@product.errorhandler(CustomException)
def customException(error):
    return error.throw_se_exception()