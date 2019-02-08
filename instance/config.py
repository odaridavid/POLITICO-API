class Config(object):
    """Parent configuration class."""
    DEBUG = False


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


# Dictionary with <K,V> mapping to available configurations
app_config = {
    'testing': TestingConfig,
    'production': ProductionConfig
}
