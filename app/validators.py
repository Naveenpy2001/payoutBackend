# validators.py
from django.core.exceptions import ValidationError
import re

def validate_username(value):
    if not re.match(r'^[A-Za-z ]+$', value):
        raise ValidationError('Username can only contain alphabetic characters and spaces.')
    if len(value) < 2 or len(value) > 30:
        raise ValidationError('Username must be between 2 and 30 characters long.')
