class PostInfoException(Exception):
    ...


class PostInfoNotFoundError(PostInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Post Info Not Found"


class PostInfoInfoAlreadyExistError(PostInfoException):

    def __init__(self):
        self.status_code = 409
        self.detail = "Post Info Already Exists"
