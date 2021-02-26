"""Initialize degoogle app."""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from degoogle_app.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.session_protection = "strong"


def create_app(config_class=Config):
    """Create an instance of degoogle app."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from degoogle_app.main.routes import main
    from degoogle_app.auth.routes import auth
    from degoogle_app.google.routes import google
    from degoogle_app.alternative.routes import alternative

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(google, url_prefix="/google")
    app.register_blueprint(alternative, url_prefix="/alternative")

    with app.app_context():
        db.create_all()

    return app
