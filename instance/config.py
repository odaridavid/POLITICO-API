import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True
    # Testing db accessed explicitly
    DATABASE_URI = os.getenv("TESTING_DATABASE_URI")


class ProductionConfig(Config):
    """Configurations for Production."""
    TESTING = False
    DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URI")


class DevelopmentConfig(Config):
    """Configurations for Development"""
    DEBUG = True
    TESTING = False
    DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URI")


# Dictionary with <K,V> mapping to available configurations
application_config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'development': DevelopmentConfig
}
