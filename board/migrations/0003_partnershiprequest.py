# Generated by Django 4.0.6 on 2022-07-08 06:48

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_options_alter_board_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnershipRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('company_name', models.CharField(max_length=15, verbose_name='회사명')),
                ('company_link', models.TextField(verbose_name='홈페이지')),
                ('manager_name', models.CharField(max_length=15, verbose_name='담당자명')),
                ('manager_phone', models.CharField(max_length=11, verbose_name='담당자 연락처')),
                ('manager_mail', models.EmailField(max_length=254, verbose_name='담당자 이메일')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='제휴제안 내용')),
                ('file', models.FileField(upload_to='', verbose_name='제휴제안서 첨부')),
                ('status', models.IntegerField(choices=[(0, '접수'), (1, '처리 중'), (2, '처리 완료')], help_text='제휴문의에 대한 내부 처리 상태 관리용입니다.', verbose_name='처리 상태')),
            ],
            options={
                'verbose_name': '제휴문의',
                'verbose_name_plural': '제휴문의',
            },
        ),
    ]
