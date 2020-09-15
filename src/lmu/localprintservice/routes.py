def includeme(config):
    config.add_static_view("static", "static", cache_max_age=3600)
    config.add_route("home", "/")
    # API Routes
    # Card API Calls
    config.add_route("stats_route", "/api/v1/", request_method="GET")
    config.add_route("cards_route", "/api/v1/cards", request_method="GET")
    config.add_route("add_card_route", "/api/v1/cards", request_method="POST")
    config.add_route("card_route", "/api/v1/cards/{card_id}", request_method="GET")
    config.add_route(
        "delete_card_route", "/api/v1/cards/{card_id}", request_method="DELETE"
    )
    # Door API Calls
    config.add_route("doors_route", "/api/v1/doors", request_method="GET")
    config.add_route("add_door_route", "/api/v1/doors", request_method="POST")
    config.add_route("door_route", "/api/v1/doors/{door_id}")
    # Open Door
    config.add_route("open_door_route", "/api/v1/open", request_method="POST")
