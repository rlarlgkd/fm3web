import os

host_name = 'mycluster-1.mycluster-instances.default.svc.cluster.local'
username = "root"
password = "dkagh1."
database_name = "test1"

base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  SECRET_KEY = 'your secret key'
  algo = 'HS256'
  DEBUG = False
  
class DevelopmentConfig(Config):
  SQLALCHEMY_DATABASE_URI = "mysql://root:dkagh1.@mycluster-1.mycluster-instances.default.svc.cluster.local:3306/test1?charset=utf8"
  DEBUG = True
  SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI = "mysql://root:dkagh1.@mycluster-1.mycluster-instances.default.svc.cluster.local:3306/test1?charset=utf8"
  DEBUG = False
  SQLALCHEMY_TRACK_MODIFICATIONS = False

config_by_name = dict(
  dev=DevelopmentConfig,
  prod=ProductionConfig,
) 

key = Config.SECRET_KEY
algorithm = Config.algo

mailConfig = ['youremail@email.com','email-password']
