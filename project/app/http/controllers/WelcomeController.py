"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request
from masonite.response import Response
from masonite.routes import Route

class WelcomeController:
    """Controller For Welcoming The User."""

    def show(self, view: View, request: Request):
        """Show the welcome page.

        Arguments:
            view {masonite.view.View} -- The Masonite view class.
            Application {config.application} -- The application config module.

        Returns:
            masonite.view.View -- The Masonite view class.
        """
        return view.render('welcome', {
            'app': request.app().make('Application')
        })

    def match(self, view: View, request: Request, response: Response, route: Route):
        print('===================')
        headers = {
            'Access-Control-Allow-Methods': 'POST, GET, OPTIONS, PUT, PATCH, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type, X-Auth-Token, Origin, Authorization',
            'Allow': 'POST, GET, PUT, PATCH, DELETE',
        }
        response.request._headers = headers
        return {}