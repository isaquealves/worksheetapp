import random
from decimal import InvalidOperation
from django.core.exceptions import ValidationError
import pytest
from django.test import TestCase

from worksheet.models import Transaction, TransactionType


def test_transaction_value(transaction):
    assert transaction.amount.__str__() == '3000.09'

def test_trasaction_type(transaction):
    assert transaction.kind == 'credit'

@pytest.mark.parametrize('name,transaction_type,amount',[
 ('test1', TransactionType.DEBIT.value, float(random.getrandbits(65))),
 ('test2', TransactionType.CREDIT.value, float(random.getrandbits(72))),
])
def test_for_invalid_decimal_values(user_ref, name, transaction_type, amount):
    with pytest.raises(InvalidOperation):
        transaction = Transaction.objects.create(user=user_ref,
                                                 name=name,
                                                 kind=transaction_type,
                                                 amount=amount)
