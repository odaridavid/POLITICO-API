from flask import Flask
from instance.config import app_config


def create_app(config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # Setup configuration
    app.config.from_object(app_config[config])
    # Return application context
    return app
