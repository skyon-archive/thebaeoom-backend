from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny

from board.models import Board, PartnershipRequest, ErrorRequest
from board.serializers import (
    BoardListSerializer,
    BoardDetailSerializer,
    PartnershipRequestSerializer,
    ErrorRequestSerializer,
)


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    search_fields = ["title", "content"]
    filterset_fields = ["type"]
    ordering = ["-id"]

    def get_serializer_class(self):
        if self.action == "list":
            return BoardListSerializer
        elif self.action == "retrieve":
            return BoardDetailSerializer

    def get_object(self):
        item = get_object_or_404(self.queryset, id=self.kwargs["pk"])
        if self.action == "retrieve":
            item.view += 1
            item.save()
        return item


class PartnershipRequestViewSet(viewsets.ModelViewSet):
    queryset = PartnershipRequest.objects.all()
    serializer_class = PartnershipRequestSerializer
    permission_classes = (AllowAny,)


class ErrorRequestViewSet(viewsets.ModelViewSet):
    queryset = ErrorRequest.objects.all()
    serializer_class = ErrorRequestSerializer
    permission_classes = (AllowAny,)
