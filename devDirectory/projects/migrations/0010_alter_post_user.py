# Generated by Django 3.2.8 on 2022-06-24 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
