import os
# import uuid

# ## Setting database url for database
os.environ['DATABASE_URL'] = 'postgres://vgoavisqcoznov:5ff042c62efe885ac3dd87d6d12ace1f16b8b4dd7e767a84bf5da31b97cdcc46@ec2-184-73-222-192.compute-1.amazonaws.com:5432/d3vjtvhujq77bp'

# # setting up secret
# os.environ['SECRET_KEY'] = str(uuid.uuid4()).strip()

# setting up environment
APP_ENV = 'local'
if( APP_ENV == 'local'):
    os.environ['APP_SETTINGS'] = 'product_importer.config.config.DevelopmentConfig'
if(APP_ENV == 'staging'):
    os.environ['APP_SETTINGS'] = 'product_importer.config.config.DevelopmentConfig'
if(APP_ENV == 'production'):
    os.environ['APP_SETTINGS'] = 'product_importer.config.config.ProductionConfig'



from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgres://vgoavisqcoznov:5ff042c62efe885ac3dd87d6d12ace1f16b8b4dd7e767a84bf5da31b97cdcc46@ec2-184-73-222-192.compute-1.amazonaws.com:5432/d3vjtvhujq77bp')
Session = sessionmaker(bind=engine)

Base = declarative_base() 
