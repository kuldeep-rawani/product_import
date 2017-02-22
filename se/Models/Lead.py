from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from se.Config.app import app, db

class lead_management(db.Model):
	#tablename
	__tablename__ = 'lead_management'

	# columns of lead_management table

	id = db.Column(db.String(100), primary_key=True)
	first_name = db.Column(db.String(30) , nullable=False)
	last_name = db.Column(db.String(30) , nullable=False)
	email = db.Column(db.String(100), unique=True , nullable=False)
	company = db.Column(db.String(50) , nullable=False)
	phone = db.Column(db.String(100) , nullable=False)
	country = db.Column(db.String(50) , nullable=False)
	state = db.Column(db.String(50) , nullable=False)
	about_project = db.Column(db.Text , nullable=False)
	project_type = db.Column(db.String(50) , nullable=False)
	sign_up_news_letter = db.Column(db.Boolean , default=False, nullable=False)
	created_at = db.Column(db.DateTime, server_default=db.func.now())
	updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
	deleted_at = db.Column(db.DateTime, nullable=True)





