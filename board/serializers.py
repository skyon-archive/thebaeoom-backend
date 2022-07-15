from typing import Union

from rest_framework import serializers

from board.models import Board, ErrorRequest, PartnershipRequest, Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("id", "title", "image", "link", "created_at")


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("id", "title", "view", "created_at", "type")


class BoardDetailSerializer(serializers.ModelSerializer):
    previous = serializers.SerializerMethodField()
    next = serializers.SerializerMethodField()
    page = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = (
            "id",
            "title",
            "view",
            "created_at",
            "content",
            "file",
            "type",
            "previous",
            "next",
            "page",
        )

    def get_previous(self, instance) -> Union[BoardListSerializer, None]:
        try:
            return BoardListSerializer(
                Board.objects.filter(id__lt=instance.id, type=instance.type).order_by(
                    "-id"
                )[0]
            ).data
        except IndexError:
            return None

    def get_next(self, instance) -> Union[BoardListSerializer, None]:
        try:
            return BoardListSerializer(
                Board.objects.filter(id__gt=instance.id, type=instance.type).order_by(
                    "id"
                )[0]
            ).data
        except IndexError:
            return None

    def get_page(self, instance) -> int:
        return (
            Board.objects.filter(id__gt=instance.id, type=instance.type).count() // 10
            + 1
        )


class PartnershipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnershipRequest
        fields = (
            "company_name",
            "company_link",
            "manager_name",
            "manager_phone",
            "manager_mail",
            "content",
            "file",
        )


class ErrorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorRequest
        fields = (
            "book",
            "title",
            "content",
            "file",
        )
