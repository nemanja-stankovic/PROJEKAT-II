
class ReservationExceptionCode(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


class ReservationNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code