
"""Conftest plugin module
This module allow sharing some data between tests
"""
import pytest
from django.contrib.auth.models import User
from worksheet.models import Transaction, TransactionType

@pytest.fixture
def user_ref(transactional_db):
    """ User fixture
    Simple fixture to return a user reference to be used on

    Args:
        transactional_db (fixture): Pytest builtin fixture to
        provide access to db
    """
    user = User.objects.create(username='john',
                               email='johndoe@example.com',
                               password='123')
    return user

@pytest.fixture
def transaction(transactional_db, user_ref):
    """Transaction fixture
    Simple fixture to provide a transaction object
    to be tested and verified
    Args:
        transactional_db (fixture): Pytest builtin fixture to
        provide access to db
        user_ref (fixture): The user_ref fixture
    """
    transaction = Transaction.objects.create(user=user_ref,
                                                    name='Salary',
                                                    kind='credit',
                                                    amount="3000.09")
    return transaction
