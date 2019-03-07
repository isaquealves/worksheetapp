""" Validators

This module contains the validators used on the application
"""

from decimal import Decimal, InvalidOperation

def positive_decimal_validate(number):
    """
    """

    try:
        value = Decimal(number)
        if value < 0:
            raise InvalidOperation(
                '***REMOVED***val***REMOVED*** should be a positive number'.format(val=value),
                code='negative number'
            )
    except (ValueError, TypeError):
        raise ValidationError('Enter a valid decimal or integer value',
                              code='invalid number')