# Generated by Django 3.2.7 on 2021-11-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]