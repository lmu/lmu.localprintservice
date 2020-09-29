from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.response import Response

import os.path
import sys


def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update({
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
        'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
        'Access-Control-Allow-Credentials': 'true',
        'Access-Control-Max-Age': '1728000',
        })
    event.request.add_response_callback(cors_headers)


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.add_subscriber(add_cors_headers_response_callback, NewRequest)
        config.include("pyramid_openapi3")
        config.pyramid_openapi3_spec(
            os.path.join(os.path.dirname(__file__), "openapi.yaml")
        )
        config.pyramid_openapi3_add_explorer()
        config.include(".routes")
        config.scan()
    print("Swagger UI available at http://127.0.0.1:6543/docs/")  # NOQA: T001
    return config.make_wsgi_app()
