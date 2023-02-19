
class AirportExceptionCode(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class AirportNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

