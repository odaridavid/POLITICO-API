from flask import Flask
# Setup Models
from .v1 import models
# Import blueprint - contain routes handling interaction between view and models
from .v1.views import version_1


# configure app prerequisites
def create_app():
    # create and configure the app
    app = Flask(__name__)
    #  Register  blueprints in app instance creation
    app.register_blueprint(version_1)
    # Return application context
    return app
