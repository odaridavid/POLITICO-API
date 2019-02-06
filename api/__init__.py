from flask import Flask, make_response, jsonify
# Setup Models
from .v1 import models
# Import blueprint - contain routes handling interaction between view and models
from .v1.views import version_1


# Error Handler Method
def page_not_found(e):
    error_response = {
        "error": "404 ERROR:PAGE NOT FOUND",
        "status": 404
    }
    return make_response(jsonify(error_response))


# configure app prerequisites
def create_app():
    # create and configure the app
    app = Flask(__name__)
    #  Register  blueprints in app instance creation
    app.register_blueprint(version_1)
    # Error Handler for error message 404
    app.register_error_handler(404, page_not_found)
    # Return application context
    return app
