# Generated by Django 2.2.5 on 2020-03-05 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191114_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
