# Generated by Django 3.2.8 on 2021-11-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersmodel',
            name='about',
            field=models.TextField(null=True, verbose_name='Обо мне'),
        ),
    ]
