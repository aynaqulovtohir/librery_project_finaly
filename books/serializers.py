from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title','subtitle','content','author','isbn','price')

    def validate(self,data):
        title = data.get('title',None)

        return data