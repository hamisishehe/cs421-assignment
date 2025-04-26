import os

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'mysql+pymysql://root:@db/hamisi-assignment')
SQLALCHEMY_TRACK_MODIFICATIONS = False
