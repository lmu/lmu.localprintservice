from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import notfound_view_config


@notfound_view_config(renderer="../templates/404.pt")
def notfound_view(request):
    request.response.status = 404
    return {}


@view_config(route_name="add_card_route", request_method="POST", openapi=True)
def print_pdf_view(request):
    card_id = request.params.get("card_id")
    lmu_id = request.params.get("lmu_id")
    return Response("OK", status=200)
