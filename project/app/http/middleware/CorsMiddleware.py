""" Cors Middleware """

from masonite.request import Request

class CorsMiddleware:
    """Cors Middleware
    """

    def __init__(self, request: Request):
        """Inject Any Dependencies From The Service Container

        Arguments:
            Request {masonite.request.Request} -- The Masonite request object
        """

        if request.header('Access-Control-Allow-Origin') != '*':
            request.header('Access-Control-Allow-Origin', '*')
            request.header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS, PUT, PATCH, DELETE')
            request.header('access-control-allow-headers', 'Content-Type, X-Auth-Token, Origin, Authorization')

        self.request = request

    def before(self):
        """Run This Middleware Before The Route Executes
        """

        pass

    def after(self):
        """Run This Middleware After The Route Executes
        """

        pass