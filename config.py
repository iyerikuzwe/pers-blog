# import os

# class Config:
#     '''
#     General configuration parent class
#     '''
#     # SECRET_KEY = 'TheDifference'
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:regineiyera@localhost/pitch3'
#     UPLOADED_PHOTOS_DEST ='app/static/photos'
    
#     #  email configurations
#     MAIL_SERVER = 'smtp.googlemail.com'
#     MAIL_PORT = 587 
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
#     MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
#     SUBJECT_PREFIX = 'One Minute Pitch'
#     SENDER_EMAIL = 'iyerikuzweregine19@gmail.com'

#     # simple mde  configurations
#     SIMPLEMDE_JS_IIFE = True
#     SIMPLEMDE_USE_CDN = True

# class TestConfig(Config):
  

# class ProdConfig(Config):
#     '''
#     Production  configuration child class
#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
   
    
# class DevConfig(Config):
#     '''
#     Development  configuration child class
#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
  


#     DEBUG = True

# config_options = {
# 'development':DevConfig,
# 'production':ProdConfig,
# 'test':TestConfig
# }
import os

class Config:

    
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:regineiyera@localhost/pitch3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'my project '
    SENDER_EMAIL = 'iyerikuzweregine19@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:regineiyera@localhost/pitch3'
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}