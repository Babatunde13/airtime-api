import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_graphql import GraphQLView
from flask_graphql_auth import GraphQLAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .schema import schema

load_dotenv()

auth = GraphQLAuth()
db = SQLAlchemy()
migrate = Migrate()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    app.config.from_object(os.environ["APP_SETTINGS"])

    db.init_app(app)
    migrate.init_app(app, db)
    auth.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    cross_origin()
    app.add_url_rule(
        "/graphql",
        view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True),
    )

    return app
