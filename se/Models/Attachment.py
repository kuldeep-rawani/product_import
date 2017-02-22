from sqlalchemy.dialects.postgresql import JSON
from flask_sqlalchemy import SQLAlchemy
from se.Config.app import app, db
from sqlalchemy.types import Text
from datetime import datetime
from flask import Flask

class lead_attachment(db.Model):
	#tablename
	__tablename__ = 'lead_attachment'

	# columns of lead_management table

	id = db.Column(db.String(100), primary_key=True)
	lead_id = db.Column(db.String(100), db.ForeignKey('lead_management.id'), nullable=False)
	attachment = db.Column(JSON, nullable=False)
	created_at = db.Column(db.DateTime, server_default=db.func.now())
	updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
	deleted_at = db.Column(db.DateTime, nullable=True)




