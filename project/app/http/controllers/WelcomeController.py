"""Welcome The User To Masonite."""

from masonite.view import View
from masonite.request import Request


class WelcomeController:

    def __init__(self, request:Request):
        if request.header('Access-Control-Allow-Origin') != '*':
            request.header('Access-Control-Allow-Origin', '*')

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
