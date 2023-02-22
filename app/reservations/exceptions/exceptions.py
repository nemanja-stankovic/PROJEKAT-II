"""It creates a class called ReservationNotFoundException that inherits from the Exception class"""

class ReservationExceptionCode(Exception):
    """It creates a class called ReservationExceptionCode that inherits from the Exception class."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class ReservationNotFoundException(Exception):
    """This class is used to raise an exception when a reservation is not found"""
    def __init__(self, message, code):
        self.message = message
        self.code = code
