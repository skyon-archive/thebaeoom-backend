from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.forms import TextInput, widgets
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from board.models import Board, PartnershipRequest, ErrorRequest, Banner


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_link", "created_at")
    list_display_links = (
        "id",
        "title",
    )
    readonly_fields = ("created_at",)

    def get_link(self, obj):
        return format_html("<a href='{url}' target='_blank'>{url}</a>", url=obj.link)

    get_link.short_description = "링크"


class BoardAdminForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = "__all__"
        widgets = {"title": TextInput(attrs={"style": "min-width: 400px;"})}


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "title", "created_at")
    list_display_links = (
        "id",
        "type",
        "title",
    )
    list_filter = ("type",)
    readonly_fields = ("view",)
    form = BoardAdminForm


@admin.register(PartnershipRequest)
class PartnershipRequestAdmin(admin.ModelAdmin):
    list_display = ("id", "company_name", "get_company_link", "status", "created_at")
    list_display_links = (
        "id",
        "company_name",
    )
    list_filter = ("status",)
    readonly_fields = ("created_at",)
    fake_readonly_fields = (
        "company_name",
        "company_link",
        "manager_name",
        "manager_phone",
        "manager_mail",
        "file",
        "content",
    )

    def get_form(self, request, obj=None, *args, **kwargs):
        form = super(PartnershipRequestAdmin, self).get_form(
            request, obj=None, *args, **kwargs
        )
        if obj:
            for field_name in self.fake_readonly_fields:
                form.base_fields[field_name].disabled = True
        return form

    def get_company_link(self, obj):
        return format_html(
            "<a href='{url}' target='_blank'>{url}</a>", url=obj.company_link
        )

    get_company_link.short_description = "홈페이지"


class ErrorRequestAdminForm(forms.ModelForm):
    class Meta:
        model = ErrorRequest
        fields = "__all__"
        widgets = {"title": TextInput(attrs={"style": "min-width: 400px;"})}


@admin.register(ErrorRequest)
class ErrorRequestAdmin(admin.ModelAdmin):
    form = ErrorRequestAdminForm
    list_display = ("id", "title", "get_book", "status", "created_at")
    list_display_links = (
        "id",
        "title",
    )
    list_filter = ("status",)
    readonly_fields = ("created_at",)
    fake_readonly_fields = (
        "book",
        "title",
        "content",
    )

    def get_form(self, request, obj=None, *args, **kwargs):
        form = super(ErrorRequestAdmin, self).get_form(
            request, obj=None, *args, **kwargs
        )
        if obj:
            for field_name in self.fake_readonly_fields:
                form.base_fields[field_name].disabled = True
        return form

    def get_book(self, obj):
        link = reverse("admin:book_book_change", args=[obj.book.isbn])
        return format_html("<a href='{url}'>{name}</a>", url=link, name=obj.book.title)

    get_book.short_description = "도서"
