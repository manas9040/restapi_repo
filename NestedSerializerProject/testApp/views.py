from django.shortcuts import render
from testApp.serializers import AuthorSerializer,BookSerializer
from testApp.models import Author,Book
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

# Create your views here.
class AuthorListAPIView(ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class AuthorAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class BookListAPIView(ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
