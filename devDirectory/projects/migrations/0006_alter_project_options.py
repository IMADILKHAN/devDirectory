# Generated by Django 3.2.8 on 2021-10-29 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20211028_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
