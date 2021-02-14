import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or "sercet key"
    # database path
    # PATH_DB = basedir
    # NAME_DB = "twitter_db.sqlite"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(PATH_DB, NAME_DB)
    # SQLALCHEMY_TRACK_MODIFICATIONS = False