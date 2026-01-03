from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameValidator:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        for c in value:
            if not (c.isalpha() or c.isspace()):
                raise ValidationError(self.message)