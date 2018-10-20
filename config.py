import os


class Config(object):

    SECRET_KEY = os.environ.get('SKY_KEY') or 'some random string'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def configure(app):
        """ override to provide configuration specific initialization """
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database-devel.sqlite3'
    BOOTSTRAP_SERVE_LOCAL = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('SKY_ADMIN_USERNAME') or 'admin@sky.com'
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    MAIL_PASSWORD = os.environ.get('SKY_ADMIN_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[Sky Blogg] '

    @staticmethod
    def configure(app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database-test.sqlite3'

    @staticmethod
    def configure(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'

    @staticmethod
    def configure(app):
        pass


config = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig
)
