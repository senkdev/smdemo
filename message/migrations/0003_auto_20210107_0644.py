# Generated by Django 3.1.4 on 2021-01-07 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20210107_0643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='username',
            field=models.CharField(default='', max_length=20, verbose_name='Kullanıcı Adı:'),
        ),
    ]