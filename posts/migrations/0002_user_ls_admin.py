# Generated by Django 2.0.7 on 2021-02-16 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ls_admin',
            field=models.BooleanField(default=False),
        ),
    ]
