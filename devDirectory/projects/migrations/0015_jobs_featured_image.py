# Generated by Django 4.1.1 on 2022-10-23 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_alter_jobs_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='featured_image',
            field=models.ImageField(blank=True, default='default-job.jpg', null=True, upload_to=''),
        ),
    ]
