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