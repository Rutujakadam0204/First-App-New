# Generated by Django 3.1.2 on 2020-10-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='image/')),
                ('price', models.PositiveIntegerField(max_length=5, primary_key=True, serialize=False)),
                ('desc', models.TextField(max_length=1000)),
                ('available', models.BooleanField(default=False)),
            ],
        ),
    ]
