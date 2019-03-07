"""Serializers module
"""

from rest_framework import serializers
from worksheet.models import Transaction
from worksheet.validators import positive_decimal_validate


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """DynamicFieldsModelSerializer

    A model serializer who takes an additional `fields` argument
    that control which fields should be displayed.
    """
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)

        super().__init__(*args, *kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field in existing - allowed:
                self.fields.pop(field)


class TransactionSerializer(DynamicFieldsModelSerializer):
    """TransactionSerializer

    Serializer for Transaction model
    """
    user = serializers.StringRelatedField(many=False)
    amount = serializers.DecimalField(max_digits=19, decimal_places=4, validators=[positive_decimal_validate])

    class Meta:
        """Meta options for serializer
        Attributes:
            model (class): The model reference
            fields (tuple): A group of fields to be displayed
        """
        model = Transaction
        fields = ['pk', 'user', 'name', 'kind', 'amount']

    def to_representation(self, obj):
        """To representation

        Override the `to_representation` method to allow displaying
        the amount values as negative in case of 'debit' transactions
        """
        data = super().to_representation(obj)
        data['amount'] = obj.amount
        if 'amount' in data and obj.kind == 'debit' :
            data['amount'] = obj.amount * -1
        return data