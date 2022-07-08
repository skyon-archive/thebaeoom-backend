from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from book.models import Book
from thebaeoom_backend.utils import get_file_upload_path

BOARD_TYPE_CHOICES = [("NOTICE", "공지사항"), ("FILE", "자료실")]
STATUS_CHOICES = [(0, "접수"), (1, "처리 중"), (2, "처리 완료")]


class Board(models.Model):
    type = models.CharField(
        choices=BOARD_TYPE_CHOICES, max_length=10, verbose_name="유형"
    )
    title = models.TextField(verbose_name="제목")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    view = models.PositiveIntegerField(default=0, verbose_name="조회수")
    content = RichTextUploadingField(verbose_name="본문")
    file = models.FileField(upload_to=get_file_upload_path, verbose_name="첨부파일")

    def __str__(self):
        return f"{self.get_type_display()} / {self.title}"

    class Meta:
        verbose_name = "게시물"
        verbose_name_plural = "보드 (공지사항/자료실)"


class PartnershipRequest(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성일",
    )
    company_name = models.CharField(
        max_length=15,
        verbose_name="회사명",
        help_text="접수된 제휴 문의는 처리 상태 외의 정보 수정이 불가능합니다.",
    )
    company_link = models.TextField(
        verbose_name="홈페이지", help_text="접수된 제휴 문의는 처리 상태 외의 정보 수정이 불가능합니다."
    )

    manager_name = models.CharField(
        max_length=15,
        verbose_name="담당자명",
        help_text="접수된 제휴 문의는 처리 상태 외의 정보 수정이 불가능합니다.",
    )
    manager_phone = models.CharField(
        max_length=11,
        verbose_name="담당자 연락처",
        help_text="접수된 제휴 문의는 처리 상태 외의 정보 수정이 불가능합니다.",
    )
    manager_mail = models.EmailField(
        verbose_name="담당자 이메일", help_text="접수된 제휴 문의는 처리 상태 외의 정보 수정이 불가능합니다."
    )

    content = RichTextUploadingField(
        verbose_name="제휴 제안 내용", help_text="접수된 제휴 문의는 처리 상태 외의 정보 수정이 불가능합니다."
    )
    file = models.FileField(
        verbose_name="제휴 제안서 첨부",
        null=True,
        blank=True,
        help_text="접수된 제휴 문의는 처리 상태 외의 정보 수정이 불가능합니다.",
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        verbose_name="처리 상태",
        help_text="제휴 문의에 대한 내부 처리 상태 관리용 상태입니다.",
        default=0,
    )

    def __str__(self):
        return f"{self.company_name}"

    class Meta:
        verbose_name = "제휴 문의"
        verbose_name_plural = "제휴 문의"


class ErrorRequest(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="생성일",
    )
    book = models.ForeignKey(
        Book,
        related_name="error_request",
        on_delete=models.CASCADE,
        verbose_name="도서",
        help_text="접수된 오류 제보는 처리 상태 외의 정보 수정이 불가능합니다.",
    )
    title = models.TextField(
        verbose_name="제목", help_text="접수된 오류 제보는 처리 상태 외의 정보 수정이 불가능합니다."
    )
    content = RichTextUploadingField(
        verbose_name="내용", help_text="접수된 오류 제보는 처리 상태 외의 정보 수정이 불가능합니다."
    )
    file = models.FileField(
        verbose_name="파일",
        null=True,
        blank=True,
        help_text="접수된 오류 제보는 처리 상태 외의 정보 수정이 불가능합니다.",
    )

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        verbose_name="처리 상태",
        help_text="오류 제보에 대한 내부 처리 상태 관리용 상태입니다.",
        default=0,
    )

    def __str__(self):
        return f"{self.book.title} / {self.title}"

    class Meta:
        verbose_name = "오류 제보"
        verbose_name_plural = "오류 제보"
