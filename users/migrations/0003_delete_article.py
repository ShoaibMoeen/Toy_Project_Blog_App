# Generated by Django 3.1.1 on 2021-02-04 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
