"""app initializer """
from api import create_app
import os


# Create app instance with env
def app_context():
    if os.getenv("FLASK_ENV") is None:
        application = create_app('testing')
        return application
    application = create_app(os.getenv("FLASK_ENV"))
    return application


app = app_context()

if __name__ == '__main__':
    app.run()
