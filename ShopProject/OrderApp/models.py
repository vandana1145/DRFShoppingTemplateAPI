from django.db import models
from datetime import datetime
from ShopApp.models import Product
from user.models import AuthUser
from model_utils import Choices

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    ORDER_STATUS = Choices(('PLACED', ('Order_PLaced')), ('DRAFTED', ('Order_in_Progress')))
    order_status = models.CharField(choices=ORDER_STATUS, default=ORDER_STATUS.DRAFTED, max_length=20)

    def get_cart_item(self, CartItem):
        return (self.CartItem.product, self.CartItem.quantity)

    def get_cart_items(self):
        return self.cartitem_set.all()

    def get_order_status(self):
        return self.order_status

# Field.choices: The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. 
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '%d- %s' %(self.quantity, self.product)

    def get_product_price(self):
        return self.product.price

    def get_total_price(self):
        return self.get_product_price() * quantity




