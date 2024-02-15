from exceptions.GException import GException


class InvalidParamException(GException):
    message = "adafa"
    code = 404

    def __init__(self, var, constraint):
        self.message = var + " must be " + constraint