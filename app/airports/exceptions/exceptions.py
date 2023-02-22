
"""The AirportExceptionCode class is a subclass of the Exception class""""


""""This class is used to raise an exception when an airport is not found"""
class AirportExceptionCode(Exception):

    def __init__(self, message, code):
        self.message = message
        self.code = code


""""This class is used to raise an exception when an airport is not found"""
class AirportNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

