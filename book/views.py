from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import SAFE_METHODS, AllowAny

from book.models import Author, Book
from book.serializers import (
    AuthorListSerializer,
    AuthorDetailSerializer,
    BookListSerializer,
    BookDetailSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    search_fields = ["name"]
    ordering = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return AuthorListSerializer
        elif self.action == "retrieve":
            return AuthorDetailSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    filterset_fields = ["is_ebook", "publisher"]
    search_fields = ["title"]
    ordering = ["created_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer
        elif self.action == "retrieve":
            return BookDetailSerializer
