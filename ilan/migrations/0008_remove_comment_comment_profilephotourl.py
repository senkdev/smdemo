# Generated by Django 3.1.4 on 2021-01-10 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0007_comment_comment_profilephotourl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_profilePhotoUrl',
        ),
    ]