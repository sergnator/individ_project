# Класс ошибок
class BasePostsException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message


class MismatchPassword(BasePostsException):
    pass


class NotFoundUsername(BasePostsException):
    pass


class NicknameIsBusy(BasePostsException):
    pass


class NoUser(BasePostsException):
    pass
