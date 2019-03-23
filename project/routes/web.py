"""Web Routes."""

from masonite.routes import Get, Post, RouteGroup

ROUTES = [
    RouteGroup([
        Get().route('/', 'WelcomeController@show').name('welcome'),
    ],
        add_methods=['OPTIONS'],
    )

]
