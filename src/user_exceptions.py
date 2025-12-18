class UserException(Exception):

    message: str

    def __init__(self, message=None):
        super().__init__(message)
        self.message = message
