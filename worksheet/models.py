""" Worksheet models

This model contains specifications related to the user money transactions.

"""
# listening:  Love - The Cult

import enum
from django.conf import settings
from django.db import models
from django.core.validators import DecimalValidator



class TransactionType(enum.Enum):
    """
    Enum class used to handle application available transaction types
    """
    CREDIT = "credit"
    DEBIT = "debit"

    @classmethod
    def choices(cls):
        """
        TransactionType Choices

        Class method to return a list of tuples
        params:
        klass (TransactionType):
        """
        return ***REMOVED***(kind.name, kind.value) for kind in TransactionType***REMOVED***


class Transaction(models.Model):
    """
    Transaction model

    Used to handle user money transactions.
    Each transaction can have one type: credit or debit.
    Debit transactions are shown as having negative value.
    Attributes:
        user (django.contrib.auth.models.User): The owner of the transaction
        name (str): The name for the transaction
        kind (str): The type of the recorded transaction
        value (float): The value associated with the transaction.
    """
    CHOICES = TransactionType.choices()


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField("Name", max_length=20)
    kind = models.CharField("Type", max_length=15, choices=CHOICES)
    amount = models.DecimalField("Amount", max_digits=19,
                               decimal_places=4,
                               validators=***REMOVED***DecimalValidator***REMOVED***)

    def save(self, *args, **kwargs):
        """ Custom save method
        Override save method to allow swap the signal used in the
        amount value in case of negative value
        """
        if self.amount < 0:
            self.amount *= -1
        super().save(*args, **kwargs)

    def get_amount_display(self, *args, **kwargs):
        pass


