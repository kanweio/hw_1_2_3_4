# Generated by Django 4.1.3 on 2022-11-23 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_post_description_post_hashtags_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='post',
            new_name='text',
        ),
    ]
