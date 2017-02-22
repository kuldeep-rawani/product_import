import os
import uuid
from env import *

## Setting database url for database
os.environ['DATABASE_URL'] = DATABASE+'://'+DATABASE_PASSWORD+':'+DATABASE_USERNAME+'@localhost/'+DATABASE_NAME

# setting up secret
os.environ['SECRET_KEY'] = str(uuid.uuid4()).strip()

# setting up environment
if( APP_ENV == 'local'):
    os.environ['APP_SETTINGS'] = 'se.Config.config.DevelopmentConfig'
if(APP_ENV == 'staging'):
    os.environ['APP_SETTINGS'] = 'se.Config.config.DevelopmentConfig'
if(APP_ENV == 'production'):
    os.environ['APP_SETTINGS'] = 'se.Config.config.ProductionConfig'
