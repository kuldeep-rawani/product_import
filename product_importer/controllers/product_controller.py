from flask import Flask, make_response, render_template
import flask
import os
from ..utils import *
from ..settings import * 
from ..models.product import Product
import uuid
# from sqlalchemy.ext.declarative import declarative_base

class ProductController():
	
	UPLOAD_FOLDER = os.getcwd()
	
	def upload_products(self, request):
		if request.form.get('url') is not None:
			data = get_csv_data_from_url(request.form.get('url'))
		elif request.files is not None:
			file = get_file(request)
			data = get_csv_data(file)
		else:
			return False
		session = Session()
		for row in data:
			name = row[0]
			sku = row[1]
			description = row[2]
			is_exist = session.query(Product).filter_by(sku=sku).first()
			if is_exist is None:
				_id = str(uuid.uuid4()).strip()
				product = Product(id=_id, name=name, sku=sku, description=description)
				session.add(product)
				session.commit()
		session.close()
		return True

	def product_filter(self, request):
		filter_params = {}
		if request.args.get('name') is not None:
			filter_params['name'] = request.args.get('name')
		if request.args.get('sku') is not None:
			filter_params['sku'] = request.args.get('sku')
		if request.args.get('is_active') is not None:
			filter_params['is_active'] = request.args.get('is_active')
		if request.args.get('is_archived') is not None:
			filter_params['is_archived'] = request.args.get('is_archived')
		session = Session()
		data = session.query(Product).filter_by(**filter_params).all()
		result = []
		for row in data:
			response = {}
			response['name'] = row.name
			response['sku'] = row.sku
			response['description'] = row.description
			response['is_active'] = row.is_active
			response['is_archived'] = row.is_archived
			result.append(response)
		return result




