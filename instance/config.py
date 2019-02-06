class Config(object):
    """Parent configuration class."""
    DEBUG = False


class TestingConfig(Config):
    """Configurations for Testing"""
    TESTING = True
    DEBUG = True


# Dictionary with <K,V> mapping to available configurations
app_config = {
    'testing': TestingConfig
}
