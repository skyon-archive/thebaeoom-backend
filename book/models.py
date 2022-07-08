from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MaxValueValidator
from django.db import models
from django_jsonform.models.fields import JSONField

from thebaeoom_backend.utils import get_file_upload_path


class Author(models.Model):
    name = models.CharField(max_length=15, verbose_name="이름")
    description = RichTextUploadingField(verbose_name="작가 소개")

    youtube_link = models.TextField(verbose_name="유튜브 링크")
    blog_link = models.TextField(verbose_name="블로그 링크")
    sns_link = models.TextField(verbose_name="SNS 링크")
    cafe_link = models.TextField(verbose_name="카페 링크")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "저자"
        verbose_name_plural = "저자"


TOC_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "keys": {
            "level": {"type": "number", "help_text": "해당 목차의 들여쓰기 단계 (1이 제일 높은 단계)"},
            "number": {"type": "string", "help_text": "해당 목차의 숫자 (ex. 1.1)"},
            "text": {"type": "string"},
        },
    },
}

BOOKSTORE_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "keys": {
            "image": {
                "type": "string",
                "choices": [
                    {"label": "텍스트 (이미지를 보여주지 않음)", "value": "NIL"},
                    {"label": "YES24", "value": "YES"},
                    {"label": "교보문고", "value": "KYO"},
                    {"label": "알라딘", "value": "ALA"},
                    {"label": "네이버 스마트스토어", "value": "NAV"},
                ],
                "default": "NIL",
                "help_text": "해당 판매 링크에 보여질 이미지를 선택합니다.",
            },
            "text": {"type": "string", "help_text": "해당 판매 링크의 판매점 이름을 입력합니다."},
            "link": {"type": "string", "help_text": "URL을 입력합니다."},
        },
    },
}


class Book(models.Model):
    isbn = models.DecimalField(
        primary_key=True,
        max_digits=13,
        decimal_places=0,
        unique=True,
        verbose_name="ISBN",
    )

    title = models.CharField(max_length=50, verbose_name="제목")
    description = RichTextUploadingField(verbose_name="도서 소개")
    author = models.ManyToManyField(Author, related_name="book", verbose_name="저자")
    publisher = models.CharField(max_length=15, verbose_name="출판사")
    pubDate = models.DateField(verbose_name="발행일", help_text="2000-00-00 형식")

    cover = models.ImageField(upload_to=get_file_upload_path, verbose_name="표지")
    price = models.PositiveIntegerField(verbose_name="정가")
    page = models.PositiveIntegerField(verbose_name="페이지")
    size = models.TextField(verbose_name="사이즈(규격)")
    category = models.CharField(max_length=15, verbose_name="분야")
    table_of_contents = RichTextUploadingField(verbose_name="목차")

    is_ebook = models.BooleanField(default=False, verbose_name="eBook 여부")

    bookstore_link = JSONField(verbose_name="구매 링크", schema=BOOKSTORE_SCHEMA)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "도서"
        verbose_name_plural = "도서"
