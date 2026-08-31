class UserAlreadyExistsError(Exception):
    pass

class EmaildoesnotExistsError(Exception):
    pass

class InvalidPasswordError(Exception):
    pass

class DbAddError(Exception):
    pass

class DbDownloadError(Exception):
    pass

class DbUpdateError(Exception):
    pass

class DbDeleteError(Exception):
    pass

class DBAssignAgentError(Exception):
    pass

class DBCehckExistsError(Exception):
    pass

class CreatinTablesError(Exception):
    pass

class GetUserIdError(Exception):
    pass

class UserLoginError(Exception):
    pass

class UserRegisterError(Exception):
    pass

class EmailisCurrentlyUseError(Exception):
    pass

class ChangeEmailError(Exception):
    pass

class DiffrentEmailError(Exception):
    pass

class ThisSamePasswordError(Exception):
    pass

class NotTheSamePasswordError(Exception):
    pass

class ChangePasswordError(Exception):
    pass

class EmptyFieldError(Exception):
    pass