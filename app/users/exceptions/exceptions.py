


class UserInvalidePassword(Exception):
    """UserInvalidePassword is a class that inherits from Exception and has two attributes: message and code."""
    def __init__(self, message, code):
        self.message = message
        self.code = code



class UserNotSuperUser(Exception):
    """It creates a new exception class called UserNotSuperUser."""
    def __init__(self, message, code):
        self.message = message
        self.code = code
