from flask import Flask
from instance.config import app_config
# Setup Models
from .v1 import models
# Import blueprint - contain routes handling interaction between view and models
from .v1.views import version_1


# configure app prerequisites
def create_app(config):
    # create and configure the app
    app = Flask(__name__)
    # Setup configuration
    app.config.from_object(app_config[config])
    #  Register  blueprints in app instance creation
    app.register_blueprint(version_1)
    # Return application context
    return app
