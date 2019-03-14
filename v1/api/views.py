"""
"""
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from worksheet.models import Transaction
from v1.api.serializers import TransactionSerializer


from django_filters.rest_framework import DjangoFilterBackend


class TransactionView(ListAPIView):
    """
    List all transactions
    """
    serializer_class= TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (OrderingFilter, )
    ordering_fields = ('name', 'amount')


class TransactionDetail(APIView):
    """
    Show details for a single instance of transaction objects
    """
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Transaction.objects.get(pk=pk)
        except  Transaction.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)

        return Response(serializer.data)

    def put(self, request, pk):

        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        transaction = self.get_object(pk)
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
