from flask import Flask
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    #logger config
    handler = logging.FileHandler("app.log")  # saves logs to a file
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
    formatter.converter = time.gmtime  # use UTC timestamps
    handler.setFormatter(formatter)

    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    from .routes import main
    app.register_blueprint(main)

    return app