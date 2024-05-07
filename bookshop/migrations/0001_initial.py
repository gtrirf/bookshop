# Generated by Django 5.0.4 on 2024-05-06 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('year', models.DateField()),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.CharField(max_length=255)),
                ('describtions', models.TextField()),
                ('isbn', models.IntegerField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='bookshop/')),
                ('year', models.DateField()),
            ],
            options={
                'db_table': 'Books',
            },
        ),
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'BooksCategory',
            },
        ),
        migrations.CreateModel(
            name='BooksAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshop.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshop.books')),
            ],
            options={
                'db_table': 'BooksAuthor',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='book_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshop.bookscategory'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('stargiven', models.FloatField(default=1)),
                ('user', models.CharField(max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookshop.books')),
            ],
            options={
                'db_table': 'review',
            },
        ),
    ]
