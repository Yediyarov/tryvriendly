# Generated by Django 3.1.5 on 2021-01-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210112_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
