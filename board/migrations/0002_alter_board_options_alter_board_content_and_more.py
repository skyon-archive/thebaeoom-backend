# Generated by Django 4.0.6 on 2022-07-08 05:43

import ckeditor_uploader.fields
from django.db import migrations, models
import thebaeoom_backend.utils


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '게시물', 'verbose_name_plural': '보드 (공지사항/자료실)'},
        ),
        migrations.AlterField(
            model_name='board',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='본문'),
        ),
        migrations.AlterField(
            model_name='board',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='생성일'),
        ),
        migrations.AlterField(
            model_name='board',
            name='file',
            field=models.FileField(upload_to=thebaeoom_backend.utils.get_file_upload_path, verbose_name='첨부파일'),
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.TextField(verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='board',
            name='type',
            field=models.CharField(choices=[('NOTICE', '공지사항'), ('FILE', '자료실')], max_length=10, verbose_name='유형'),
        ),
        migrations.AlterField(
            model_name='board',
            name='view',
            field=models.PositiveIntegerField(default=0, verbose_name='조회수'),
        ),
    ]