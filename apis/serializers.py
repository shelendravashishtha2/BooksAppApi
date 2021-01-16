from rest_framework import serializers
from .models import *
from drf_extra_fields.fields import Base64ImageField


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'
        lookup_field = "branch_text"


class CategorySerializer(serializers.ModelSerializer):
    branch_text = BranchSerializer()
    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = "category_text"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        lookup_field = "user_mail"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        lookup_field = "book_serial_id"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        lookup_field = "transaction_id"


