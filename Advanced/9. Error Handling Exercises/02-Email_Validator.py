class NameTooShortError(Exception):
    def __init__(self):
        message = 'Name must be more than 4 characters'
        super(NameTooShortError, self).__init__(message)


class MustContainAtSymbolError(Exception):
    def __init__(self):
        message = 'Email must contain @'
        super(MustContainAtSymbolError, self).__init__(message)


class InvalidDomainError(Exception):
    def __init__(self):
        message = 'Domain must be one of the following: .com, .bg, .org, .net'
        super(InvalidDomainError, self).__init__(message)


possible_domains = ['net', 'bg', 'org', 'com']
while True:
    email = input()
    if email == 'End':
        break
    if '@' not in email:
        raise MustContainAtSymbolError
    name, rest = email.split('@')
    if len(name) <= 4:
        raise NameTooShortError
    rest, domain = email.split('.')
    if domain not in possible_domains:
        raise InvalidDomainError



