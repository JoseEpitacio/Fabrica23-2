from rest_framework import serializers
from apps.autor.models import Author

class AuthorSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=0, max_value=150)

    class Meta:
        model = Author
        fields = ["id", "name", "age"]