# Generated by Django 3.1.4 on 2024-04-30 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
