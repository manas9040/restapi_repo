from testApp.models import Author,Book
from rest_framework.serializers import ModelSerializer
class BookSerializer(ModelSerializer):
     class Meta:
         model=Book
         fields='__all__'

class AuthorSerializer(ModelSerializer):
    book_by_author=BookSerializer(read_only=True,many=True)
    class Meta:
         model=Author
         fields='__all__'
