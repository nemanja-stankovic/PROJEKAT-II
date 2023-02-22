"""The AirportExceptionCode class is a subclass of the Exception class"""


class AirportExceptionCode(Exception):
    """"This class is used to raise an exception when an airport is not found"""
    def __init__(self, message, code):
        """
        The function __init__() is a constructor that initializes the class with the parameters message and code
        @param message - The message that will be displayed to the user.
        @param code - The HTTP status code
        """
        self.message = message
        self.code = code


class AirportNotFoundException(Exception):
    """"This class is used to raise an exception when an airport is not found"""
    def __init__(self, message, code):
        """
        The function __init__() is a constructor that initializes the class with the parameters message and code
        @param message - The message that will be displayed to the user.
        @param code - The HTTP status code
        """
        self.message = message
        self.code = code


