# Generated by Django 3.2.8 on 2021-10-29 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
    ]
