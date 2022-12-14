# Generated by Django 4.0.4 on 2022-08-31 03:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_video',
            field=models.FileField(default=django.utils.timezone.now, upload_to='post/post_video'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, null=True, upload_to='post/post_image'),
        ),
    ]
