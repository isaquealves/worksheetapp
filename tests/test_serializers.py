"""Serializer's tests module

This module contains tests for serializers
"""
import pytest
from worksheet.models import Transaction
from v1.api.serializers import TransactionSerializer


def test_has_expected_fields(transaction):
    serializer = TransactionSerializer(transaction)
    assert set(serializer.data.keys()) == set(***REMOVED***'user', 'name', 'kind', 'amount'***REMOVED***)

def test_allow_filter_fields(transaction):
    field_list = ***REMOVED***'name', 'amount'***REMOVED***
    serializer = TransactionSerializer(transaction, fields=field_list)
    assert set(serializer.data.keys()) == set(field_list)


