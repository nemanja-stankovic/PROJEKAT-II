
class FlightExceptionCode(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class FlightNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code