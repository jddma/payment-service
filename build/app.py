from flask import Flask

from build.urls import register_apis


def create_app(name: str) -> Flask:
    app = Flask(name)
    app.url_map.strict_slashes = False

    register_apis(app)
    return app
