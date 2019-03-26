"""Web Routes."""

from masonite.routes import Get, Post, RouteGroup
from masonite.helpers.routes import get, post, put, patch, delete, match

ROUTES = [
    #Get().route('/', 'WelcomeController@show').name('welcome'),

    RouteGroup([
        Get().route('/', 'WelcomeController@show').name('welcome'),
        match(['OPTIONS', 'HEAD'], '/', 'WelcomeController@match'),
    ])
]
