from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from app.categories import bp as categories_bp
    app.register_blueprint(categories_bp, url_prefix='/api/categories')

    from app.items import bp as items_bp
    app.register_blueprint(items_bp, url_prefix='/api/items')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/api/users')

    return app


from app import models
