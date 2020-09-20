def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    # API Routes
    config.add_route("get_printer_route", "/api/v1/printers", request_method="GET")
    config.add_route("print_pdf_route_post", "/api/v1/printpdf", request_method="POST")
    config.add_route("print_pdf_route_put", "/api/v1/printpdf", request_method="PUT")
