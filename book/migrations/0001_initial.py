# Generated by Django 4.0.6 on 2022-07-08 04:08

import django.core.validators
from django.db import migrations, models
import thebaeoom_backend.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('youtube_link', models.TextField()),
                ('blog_link', models.TextField()),
                ('sns_link', models.TextField()),
                ('cafe_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True, validators=[django.core.validators.MaxValueValidator(9999999999999)])),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=15)),
                ('pubDate', models.DateField()),
                ('cover', models.ImageField(upload_to=thebaeoom_backend.utils.get_file_upload_path)),
                ('price', models.PositiveIntegerField()),
                ('page', models.PositiveIntegerField()),
                ('size', models.TextField()),
                ('category', models.CharField(max_length=15)),
                ('table_of_contents', models.JSONField()),
                ('is_ebook', models.BooleanField(default=False)),
                ('bookstore_link', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(related_name='book', to='book.author')),
            ],
        ),
    ]
