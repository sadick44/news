# Generated by Django 4.2.3 on 2023-07-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_rename_image_description_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_viewable',
            field=models.BooleanField(default=True),
        ),
    ]
