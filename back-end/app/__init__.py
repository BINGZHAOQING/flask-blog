# encoding=utf-8
# __Author__: BingZhaoQing
# __Date__: 2020-11-16


from flask import Flask
from flask_cors import CORS
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # enable CORS
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # 注册blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    return app


from app import models

# if __name__ == '__main__':
#     app = create_app()
#     app.run()
