# Generated by Django 3.1.6 on 2021-03-03 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0004_auto_20210303_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='item_status',
        ),
    ]
