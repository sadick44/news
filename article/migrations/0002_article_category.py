# Generated by Django 4.2.3 on 2023-07-10 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, choices=[('politiques', 'politiques'), ('economies', 'economies'), ('security', 'security'), ('souvereignty', 'souvereignty'), ('other', 'other')], max_length=60),
        ),
    ]