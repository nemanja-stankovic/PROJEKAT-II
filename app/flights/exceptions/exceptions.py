

class FlightExceptionCode(Exception):
    """The FlightExceptionCode class is a subclass of the Exception class."""
    def __init__(self, message, code):
        self.message = message
        self.code = code


class FlightNotFoundException(Exception):
    """This class is a custom exception that is raised when a flight is not found"""
    def __init__(self, message, code):
        self.message = message
        self.code = code
