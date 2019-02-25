"""app initializer """
from api import create_app
import os
from flask import redirect, make_response, jsonify


# Create app instance with env
def app_context():
    if os.getenv("FLASK_ENV") is None:
        application = create_app('testing')
        return application
    application = create_app(os.getenv("FLASK_ENV"))
    return application


app = app_context()


# Create a URL route in our application for "/"
@app.route('/docs')
def home():
    return redirect('https://politicoapi2.docs.apiary.io/#', 301,
                    make_response(jsonify({"message": "redirecting to documentation"})))


if __name__ == '__main__':
    app.run()
