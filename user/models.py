from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.
class User(models.Model):
    user = models.OneToOneField(AuthUser, null=True, blank=True, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to="profile_images", blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #     return reverse("user_detail", kwargs={"pk": self.pk})
    
