from flask import Flask, make_response, jsonify
# Setup Models
from .v1 import models
# Import blueprint - contain routes handling interaction between view and models
from .v1.views.office_view import office_api
from .v1.views.party_view import party_api
from .v1.views.user_view import user_api
from .v1.views.petition_view import petition_api
from instance.config import app_config


# Error Handler Method
def page_not_found(e):
    error_response = {
        "error": "404 ERROR:REQUESTED DATA NOT FOUND",
        "status": 404
    }
    return make_response(jsonify(error_response), 404)


# configure app prerequisites
def create_app(config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config])
    #  Register  blueprints in app instance creation
    app.register_blueprint(office_api)
    app.register_blueprint(party_api)
    app.register_blueprint(user_api)
    app.register_blueprint(petition_api)
    # Error Handler for error message 404
    app.register_error_handler(404, page_not_found)
    # Return application context
    return app
