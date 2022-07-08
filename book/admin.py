from ajax_select import register, LookupChannel
from ajax_select.admin import AjaxSelectAdmin
from ajax_select.fields import AutoCompleteSelectMultipleField
from django import forms
from django.contrib import admin
from django.forms import TextInput

from book.models import Author, Book


@register("author")
class AuthorLookup(LookupChannel):
    model = Author

    def get_query(self, q, request):
        return self.model.objects.filter(name__icontains=q).order_by("name")[:50]

    def format_item_display(self, item):
        return "<span class='tag'>%s</span>" % item.name


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        widgets = {
            "isbn": TextInput(attrs={"style": "min-width: 200px;"}),
            "title": TextInput(attrs={"style": "min-width: 400px;"}),
            "size": TextInput(attrs={"style": "min-width: 400px;"}),
        }

    author = AutoCompleteSelectMultipleField("author")


@admin.register(Book)
class BookAdmin(AjaxSelectAdmin):
    form = BookAdminForm
    list_display = ("title", "작가", "publisher", "isbn")
    list_display_links = ("title",)
    search_fields = ("title", "description", "author__name", "publisher", "category")
    search_help_text = "제목, 도서 소개, 작가, 출판사, 분야로 검색"
    list_filter = ("publisher",)

    def 작가(self, obj):
        return "\n".join([author.name for author in obj.author.all()])


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"
        widgets = {
            "youtube_link": TextInput(attrs={"style": "min-width: 400px;"}),
            "blog_link": TextInput(attrs={"style": "min-width: 400px;"}),
            "sns_link": TextInput(attrs={"style": "min-width: 400px;"}),
            "cafe_link": TextInput(attrs={"style": "min-width: 400px;"}),
        }


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    form = AuthorAdminForm
