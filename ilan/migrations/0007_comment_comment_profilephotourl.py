# Generated by Django 3.1.4 on 2021-01-10 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ilan', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_profilePhotoUrl',
            field=models.CharField(default='Photo/defaultProfilePic.png', max_length=200, verbose_name='Fotoğraf Url'),
        ),
    ]