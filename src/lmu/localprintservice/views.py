from pyramid.response import Response
from pyramid.view import view_config
from pyramid.view import notfound_view_config

import base64
import glob
import json
import os.path
import sys
import tempfile


def get_default_printer():
    if sys.platform == "win32":
        from win32 import win32print
        return win32print.GetDefaultPrinter()
    else:
        import cups
        conn = cups.Connection()
        printers = []
        default_printer = conn.getDefault()
        cups_printers = conn.getPrinters()
        printers.append(default_printer) if default_printer else None
        for printer in cups_printers:
            if printer != default_printer and \
                not any(
                    elem in printer
                    for elem
                    in ["Fax", "PDF"]
                ):
                printers.append(printer)
        if not default_printer:
            default_printer = printers[0]
        return default_printer


@view_config(route_name="get_printer_route", request_method="GET", renderer="json", openapi=True)
def list_printer_view(request):
    printers = []
    if sys.platform == "win32":
        from win32 import win32print
        default_printer = win32print.GetDefaultPrinter()
        printers.append(default_printer)
        for printer in win32print.EnumPrinters(2):
            if printer[2] != default_printer and \
                not any(
                    elem in printer[2]
                    for elem
                    in ["Fax", "OneNote", "Microsoft XPS Document Writer", "Microsoft Print to PDF"]):
                printers.append(printer[2])
    else:
        import cups
        conn = cups.Connection()
        cups_printers = conn.getPrinters()
        default_printer = conn.getDefault()
        printers.append(default_printer) if default_printer else None
        for printer in cups_printers:
            if printer != default_printer and \
                not any(
                    elem in printer
                    for elem
                    in ["Fax", "PDF"]
                ):
                printers.append(printer)
    request.response.status = 200
    request.response.headers.update({
        'Access-Control-Allow-Origin': '*',
    })
    return printers


@view_config(route_name="print_pdf_route_post", request_method="POST", openapi=False)
def print_pdf_post_view(request):
    breakpoint()
    printer_id = request.params.get("printer")
    files = request.params.get(files)
    #if not pdf_files or not printer_id:
    #    return Response("Bad Request", status=400)
    with tempfile.TemporaryDirectory(suffix="lmu.localprintservice") as dir:
        with open(os.path.join(os.path.abspath(dir), "file_to_print.pdf"), "w+b") as pdf:
            pdf.write(base64.b64decode(request.body))

        files_to_print = glob.glob(os.path.join(os.path.abspath(dir), "*.pdf"))
        #breakpoint()
        if sys.platform == "win32":
            from win32 import win32print
            return win32print.GetDefaultPrinter()
        else:
            import cups
            conn = cups.Connection()
            printer = "HP_LaserJet_400_colorMFP_M475dn"
            conn.printFiles(printer, files_to_print, "Test", {})
    return Response("Created", status=201)

    return Response("Created", status=201)


@view_config(route_name="print_pdf_route_put", request_method="PUT", openapi=True)
def print_pdf_put_view(request):
    printer = request.params.get("printer") if request.params.get("printer") else get_default_printer()
    if not request.body:
        return Response("Bad Request", status=400)
    #pdf_file = request.params.get("pdf_file")
    with tempfile.TemporaryDirectory(suffix="lmu.localprintservice") as dir:
        with open(os.path.join(os.path.abspath(dir), "file_to_print.pdf"), "w+b") as pdf:
            pdf.write(request.body)
        files_to_print = glob.glob(os.path.join(os.path.abspath(dir), "*.pdf"))
        if sys.platform == "win32":
            from win32 import win32print
            return win32print.GetDefaultPrinter()
        else:
            import cups
            conn = cups.Connection()
            breakpoint()
            options = {
                "media": "A4",
                "InputSlot": "Tray2",
                "orientation-requested": "4",  # "landscape",
                "fit-to-page": "true",
                "print-quality": "5",
                "sides": "two-sided-long-edge",
            }
            conn.printFiles(printer, files_to_print, "Test", options)
    return Response("Created", status=201)


@notfound_view_config(renderer="json")
def notfound_view(request):
    request.response.status = 404
    print(f"URL not found: {request.url}")
    return {}
