from rest_framework import serializers
from .models import *

class BooksSerialzers(serializers.ModelSerializer):

    class Meta:
        model=Books
        fields="__all__"