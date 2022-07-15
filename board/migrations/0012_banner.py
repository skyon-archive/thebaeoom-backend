# Generated by Django 4.0.6 on 2022-07-15 02:42

from django.db import migrations, models
import thebaeoom_backend.utils


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0011_alter_board_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, verbose_name='제목')),
                ('image', models.ImageField(upload_to=thebaeoom_backend.utils.get_file_upload_path, verbose_name='이미지')),
                ('link', models.TextField(verbose_name='링크')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
            ],
        ),
    ]