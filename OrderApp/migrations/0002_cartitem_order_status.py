# Generated by Django 3.1.6 on 2021-03-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='order_status',
            field=models.CharField(choices=[('PLACED', 'Order_PLaced'), ('DRAFTED', 'Order_in_Progress')], default='DRAFTED', max_length=20),
        ),
    ]
