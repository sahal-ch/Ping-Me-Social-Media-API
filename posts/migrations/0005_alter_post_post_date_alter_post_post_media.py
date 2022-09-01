# Generated by Django 4.0.4 on 2022-09-01 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_media',
            field=models.FileField(blank=True, null=True, upload_to='post/post_media'),
        ),
    ]
