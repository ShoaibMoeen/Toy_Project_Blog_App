# Generated by Django 3.1.1 on 2021-02-04 11:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.datetime.now)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=8000)),
                ('status', models.CharField(default='pending', max_length=255)),
                ('edited_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Editor', to=settings.AUTH_USER_MODEL)),
                ('written_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
