from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import notfound_view_config

from win32 import win32print

@notfound_view_config(renderer="json")
def notfound_view(request):
    request.response.status = 404
    return {}



@view_config(route_name="get_printer_route", request_method="GET", openapi=True, renderer="json")
def print_pdf_view(request):
    printers = []
    default_printer = win32print.GetDefaultPrinter()
    printers.add(default_printer)
    for printer in win32print.EnumPrinters(2):
        if printer[2] != default_printer and "Fax" not in printer[2] and "OneNote" not in printer[2]:
            printers.add(printer)

    request.response.body = printers
    request.response.status = 200
    return request.response

@view_config(route_name="print_pdf_route", request_method="POST", openapi=True)
def print_pdf_view(request):
    printer_id = request.params.get("printer")
    pdf_file = request.params.get("pdf_file")
    print(printer_id)
    return Response("OK", status=201)
