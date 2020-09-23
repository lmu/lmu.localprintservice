from pyramid.config import Configurator

import os.path
import sys


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include("pyramid_openapi3")
        config.pyramid_openapi3_spec(
            os.path.join(os.path.dirname(__file__), "openapi.yaml")
        )
        config.pyramid_openapi3_add_explorer()
        config.include(".routes")
        config.scan()
    print("Swagger UI available at http://127.0.0.1:6543/docs/")  # NOQA: T001
    return config.make_wsgi_app()
