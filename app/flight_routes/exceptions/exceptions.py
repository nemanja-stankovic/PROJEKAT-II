
class RouteExceptionCode(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class RouteNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
