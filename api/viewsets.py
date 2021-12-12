from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Author,Book,SaleItem
from .serializer import AuthorSerializer,BookSerializer,SaleItemSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    serializer_class = BookSerializer

class SaleItemsViewSet(viewsets.ModelViewSet):
    queryset=SaleItem.objects.all()
    serializer_class=SaleItemSerializer