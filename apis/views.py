from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class UserAPI(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "user_mail"
    lookup_value_regex = "[^/]+"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()

        return Response({'message': 'Item has been deleted'})

class BranchAPI(viewsets.ModelViewSet):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    lookup_field = "branch_text"
    lookup_value_regex = "[^/]+"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()

        return Response({'message': 'Item has been deleted'})

class BookAPI(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "book_serial_id"
    lookup_value_regex = "[^/]+"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book_category','sold_by','bought_by']

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()
        book.delete()

        return Response({'message': 'Item has been deleted'})

class PaymentAPI(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    lookup_field = "transaction_id"
    lookup_value_regex = "[^/]+"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        payment = self.get_object()
        payment.delete()

        return Response({'message': 'Item has been deleted'})

class CategoryAPI(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "category_text"
    lookup_value_regex = "[^/]+"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()

        return Response({'message': 'Item has been deleted'})
