from flask import Flask
from app.database import init_db

def create_app():
    app=flask(__name__)
    app.config['DATABASE']='queries.db'

    init_db(app)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
