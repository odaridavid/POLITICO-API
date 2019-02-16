"""app initializer """
from api import create_app
import os

# Create app instance with env
app = create_app(os.getenv("FLASK_ENV"))

if __name__ == '__main__':
    app.run()
