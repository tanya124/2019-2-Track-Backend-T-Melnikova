# Generated by Django 2.2.5 on 2019-11-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191114_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='new_messages',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
