from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=100, db_index=True, verbose_name='category', default='Clothings')

    def __str__(self):
        return (self.category)

    # def get_absolute_url(self):
    #     return reverse("category_detail", kwargs={"pk": self.pk})

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name="category_name", on_delete=models.CASCADE)
    product = models.CharField(max_length=100, verbose_name='product', default='Nil')
    product_image = models.ImageField(upload_to="product_images", blank=True)
    description = models.TextField(blank=True, verbose_name='description')
    size = models.CharField(max_length=4, verbose_name='size', blank=True)
    price = models.FloatField(blank=True, verbose_name='price', default=0)

    def __str__(self):
        return (self.product)

    # def get_absolute_url(self):
    #     return reverse("product_detail", kwargs={"pk": self.pk})
    

# class Choice(models.Model):
#     product = models.ForeignKey(Product, related_name='product_name', verbose_name='item', on_delete=models.CASCADE)
#     size = models.CharField(max_length=4, verbose_name='size')
#     price = models.FloatField(blank=True, verbose_name='price')

#     def __str__(self):
#         return str(self.product)
    