# Generated by Django 3.1.6 on 2021-03-01 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(db_index=True, default='Clothings', max_length=100, verbose_name='category'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=0, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.CharField(default='Nil', max_length=100, verbose_name='product'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, upload_to='product_images'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=4, verbose_name='size'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
