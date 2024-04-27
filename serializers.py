# quotes/serializers.py
from rest_framework import serializers
from .models import Quote, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'date_of_birth']

class QuoteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'source', 'creation_date']
