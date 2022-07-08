from rest_framework import serializers

from board.models import Board, ErrorRequest, PartnershipRequest


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("id", "title", "view", "created_at")


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ("id", "title", "view", "created_at", "content", "file")


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
