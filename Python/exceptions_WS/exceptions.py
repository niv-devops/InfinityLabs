class TooShortExeception(Exception):
    def __init__(self, message="Password length must be at least 8 characters."):
        self.message = message
        super().__init__(message)

class NoUpperCaseExeception(Exception):
    def __init__(self, message="Password must include at least one uppercase letter."):
        self.message = message
        super().__init__(message)

class NoLowerCaseExeception(Exception):
    def __init__(self, message="Password must include at least one lowercase letter."):
        self.message = message
        super().__init__(message)

class NoNumberExeception(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(message)
    def __str__(self):
        self.message = "Password must include at least one digit."

class NoSymbloExeception(Exception):
    def __init__(self, message="Password must include at least one of these signs: ['@' '#' '%' '&']"):
        self.message = message
        super().__init__(message)