# Generated by Django 4.2.3 on 2023-07-11 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image_description',
            new_name='image',
        ),
    ]
