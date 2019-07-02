from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_ckeditor import CKEditor
from flask_migrate import Migrate
from flask_login import LoginManager


db = SQLAlchemy()
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
ckeditor = CKEditor()
migrate = Migrate()
login_manager = LoginManager()
