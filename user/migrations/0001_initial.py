# Generated by Django 3.1.4 on 2021-01-06 18:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Ad')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Soyad')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='E-mail')),
                ('about', models.CharField(blank=True, max_length=150, null=True, verbose_name='Hakkında')),
                ('photo', models.FileField(blank=True, null=True, upload_to='Photo/')),
                ('instagram', models.CharField(blank=True, max_length=30, null=True, verbose_name='İnstagram')),
                ('twitter', models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=30, null=True, verbose_name='Twitter')),
                ('facebook', models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=30, null=True, verbose_name='Facebook')),
                ('high_school', models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=50, null=True, verbose_name='Lise')),
                ('university', models.CharField(blank=True, help_text='Profil linkinizi koyunuz.', max_length=50, null=True, verbose_name='Üniversite')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
