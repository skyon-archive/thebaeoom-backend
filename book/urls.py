from django.urls import path

from book.views import AuthorViewSet, BookViewSet

urlpatterns = [
    path("books", BookViewSet.as_view({"get": "list"})),
    path("books/<int:pk>", BookViewSet.as_view({"get": "retrieve"})),
    path("authors", AuthorViewSet.as_view({"get": "list"})),
    path("authors/<int:pk>", AuthorViewSet.as_view({"get": "retrieve"})),
]
