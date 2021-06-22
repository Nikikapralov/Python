from django.core.exceptions import ValidationError


def name_fst_letter_capital(name):
    if name[0] != name[0].upper():
        raise ValidationError('First letter must be capital!')


def password_only_letters_and_numbers(password):
    if not all([True if char.isalnum() else False for char in password]):
        raise ValidationError('Only alphanumeric characters are permitted!')