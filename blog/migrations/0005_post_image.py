# Generated by Django 2.2.26 on 2022-03-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220324_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='blog_post_images/% Y/% m/% d/'),
            preserve_default=False,
        ),
    ]
