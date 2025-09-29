class PasswordTooShortError(Exception):
    pass
class PasswordTooCommonError(Exception):
    pass
class PasswordNoSpecialCharactersError(Exception):
    pass
class PasswordContainsSpacesError(Exception):
    pass

def password_too_common(pwd, special_chars):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_specials = all(char in special_chars for char in pwd)
    return only_digits or only_letters or only_specials

SPECIAL_SYMBOLS = ["@", "*", "&", "%"]

while (password:=input()) != "Done":
    if len(password) < 8:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if password_too_common(password, SPECIAL_SYMBOLS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(char in SPECIAL_SYMBOLS for char in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid")