from rest_framework import serializers

from book.models import Book, Author


class BookPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("isbn", "cover", "pubDate")


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name")


class AuthorDetailSerializer(serializers.ModelSerializer):
    book = BookPreviewSerializer(many=True)

    class Meta:
        model = Author
        fields = (
            "id",
            "name",
            "description",
            "youtube_link",
            "blog_link",
            "sns_link",
            "cafe_link",
            "book",
        )

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["book"] = sorted(
            response["book"], key=lambda x: x["pubDate"], reverse=True
        )
        return response


class AuthorPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("id", "name", "description")


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("name",)


class BookListSerializer(serializers.ModelSerializer):
    author = AuthorNameSerializer(many=True)

    class Meta:
        model = Book
        fields = ("isbn", "title", "author", "publisher", "pubDate", "price", "cover")


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorPreviewSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            "title",
            "author",
            "publisher",
            "pubDate",
            "price",
            "cover",
            "isbn",
            "page",
            "size",
            "category",
            "description",
            "table_of_contents",
            "bookstore_link",
        )
