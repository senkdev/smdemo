# Generated by Django 3.1.4 on 2021-01-02 20:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ilan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilan',
            name='content',
            field=models.TextField(verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='ilan',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='ilan',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='İlan Sahibi'),
        ),
        migrations.AlterField(
            model_name='ilan',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]