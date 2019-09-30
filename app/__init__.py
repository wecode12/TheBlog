from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_simplemde import SimpleMDE
from flask_moment import Moment

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
from flask_mail import Mail



bootstrap = Bootstrap()
db = SQLAlchemy()
simple = SimpleMDE()
moment = Moment()




photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    login_manager.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # configure UploadSet
    configure_uploads(app,photos)
    mail.init_app(app)
    simple.init_app(app)

    # Will add the views and forms
    
    

    return app