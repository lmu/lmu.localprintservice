from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import notfound_view_config

from win32 import win32print

import json

@view_config(route_name="get_printer_route", request_method="GET", renderer="json", openapi=True)
def list_printer_view(request):
    printers = []
    default_printer = win32print.GetDefaultPrinter()
    printers.append(default_printer)
    for printer in win32print.EnumPrinters(2):
        if printer[2] != default_printer and \
            not any(
                elem in printer[2] 
                for elem 
                in ["Fax", "OneNote", "Microsoft XPS Document Writer", "Microsoft Print to PDF"]):
            printers.append(printer[2])
            
    request.response.status = 200
    return printers


@view_config(route_name="print_pdf_route", request_method="POST", openapi=True)
def print_pdf_view(request):
    printer_id = request.params.get("printer")
    pdf_file = request.params.get("pdf_file")
    print(printer_id)
    return Response("OK", status=201)

@notfound_view_config(renderer="json")
def notfound_view(request):
    request.response.status = 404
    print(f"URL not found: {request.url}")
    return {}
