"""app initializer """
from api import create_app
import os


# Create app instance with env
def app_context():
    if os.getenv("FLASK_ENV") is None:
        app = create_app('testing')
        return app
    app = create_app(os.getenv("FLASK_ENV"))
    return app


if __name__ == '__main__':
    app_context().run()
