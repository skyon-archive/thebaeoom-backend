from django.urls import path

from board.views import BoardViewSet, PartnershipRequestViewSet, ErrorRequestViewSet

urlpatterns = [
    path("boards", BoardViewSet.as_view({"get": "list"})),
    path("boards/<int:pk>", BoardViewSet.as_view({"get": "retrieve"})),
    path("partnerships", PartnershipRequestViewSet.as_view({"post": "create"})),
    path("errors", ErrorRequestViewSet.as_view({"post": "create"})),
]
