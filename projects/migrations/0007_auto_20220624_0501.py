# Generated by Django 3.2.8 on 2022-06-24 05:01

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('caption', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('no_of_like', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created', '-vote_ratio', '-vote_total', 'title']},
        ),
    ]