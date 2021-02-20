import os
from flask import Flask

SERVER_ID = os.environ['SERVER_ID']  # just an environment variable


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        message = 'Hello World!' + '<br>' + 'Server ID : ' + SERVER_ID
        return message

    return app


# development server
if __name__ == '__main__':
    app = create_app()
    app.run()
