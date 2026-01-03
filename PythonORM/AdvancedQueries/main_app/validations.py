from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class RatingValidator:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        if not 0<=value<=10:
            raise ValidationError(self.message)

@deconstructible
class ReleaseYearValidator:
    def __init__(self, message):
        self.message = message

    def __call__(self, value):
        if not 1990<=value<=2023:
            raise ValidationError(self.message)




























