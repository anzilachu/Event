# Generated by Django 4.1.7 on 2023-03-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_subscribe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image3',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='posts/'),
        ),
        migrations.AddField(
            model_name='post',
            name='image4',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='posts/'),
        ),
    ]
