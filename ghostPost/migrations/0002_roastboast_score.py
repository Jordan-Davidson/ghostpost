# Generated by Django 3.0.6 on 2020-05-18 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ghostPost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roastboast',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]