"""app initializer """
from api import create_app

"""defining the configuration to be used"""
app = create_app(config="testing")


# For Test Purposes
@app.route('/')
def hello():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run()
