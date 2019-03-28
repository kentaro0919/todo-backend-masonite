from masonite.routes import Get, Post, Delete, Patch, Redirect, RouteGroup

ROUTES = [
    RouteGroup(
        [
            Get().route("", "TodosController@index"),
            Post().route("", "TodosController@create"),
            Delete().route("", "TodosController@deleteAll"),
            ],
        name="todos.",
        prefix="/",
        add_methods=["OPTIONS"],
        ),
    RouteGroup(
        [
            Get().route("@id", "TodosController@show"),
            Patch().route("@id", "TodosController@update"),
            Delete().route("@id", "TodosController@delete"),
            ],
        name="todo.",
        prefix="/",
        add_methods=["OPTIONS"],
        ),
    ]
