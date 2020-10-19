# Generated by Django 3.1.2 on 2020-10-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_side', '0007_book_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('admin', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
