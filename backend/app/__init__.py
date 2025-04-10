from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink
from app.admin import AdminView
from wtforms.fields import SelectField
from flask_mail import Mail



db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_message = ('Please log in to access this page.')
login.login_view = "main.login"
bootstrap = Bootstrap()
mail = Mail()


class ProductModelView(ModelView):

    form_overrides = dict(
        category=SelectField
    )
    form_args = dict(
        category=dict(
            choices=[
                ('BALM','Balm'),
                ('WAX','Wax'),
                ('CREAM', 'Cream'),
                ('ACCESSORY', 'Accessory'),
                ('CONDITIONER', 'Conditioner'),
                ('SOFTENER', 'Softener')
            ]
        )
    )



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)


    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)


    from app.main import bp as main_bp
    app.register_blueprint(main_bp)


    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')


    admin=Admin(app, name='Beard Bros', index_view=AdminView(User, db.session, url='/bro', endpoint='admin'), template_mode='bootstrap3')
    admin.add_view(ProductModelView(Product, db.session))
    admin.add_view(ModelView(Role, db.session))
    admin.add_view(ModelView(Feedback, db.session))
    #admin.add_view(SnipCart(name='SnipCart', endpoint='SnipCart'))
    admin.add_link(MenuLink(name='Back Home', url='/'))



    return app



from app import models
from app.models import User, Product, UserSchema, ProductSchema, Feedback, Role, Product
