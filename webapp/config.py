import webapp.credentionals as cred
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or "DFGRTH@#vdr534wcvi"

    # Variables that contains the user credentials to access Twitter API
    # ACCESS_TOKEN    = cred.__dict__.get('ACCESS_TOKEN',     '')
    # ACCESS_SECRET   = cred.__dict__.get('ACCESS_SECRET',    '')
    # CONSUMER_KEY    = cred.__dict__.get('CONSUMER_KEY',     '')
    # CONSUMER_SECRET = cred.__dict__.get('CONSUMER_SECRET',  '')



    # database path
    # PATH_DB = basedir
    # NAME_DB = "twitter_db.sqlite"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PATH_DB, NAME_DB)
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
