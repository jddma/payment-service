from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from build import url
from controllers.payment_controller import PaymentController


def configure_swagger(app: Flask) -> Flask:
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='Awesome Project',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0.0'
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
    })
    return app


def register_urls(api: Api, docs) -> Api:
    api.add_resource(PaymentController, url('/payment'))
    docs.register(PaymentController)
    return api


def register_apis(app: Flask) -> Flask:
    configure_swagger(app)
    api = Api(app)
    docs = FlaskApiSpec(app)
    register_urls(api, docs)
    return app
