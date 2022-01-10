from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = models.CharField(max_length=50,default="")
    state = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    street = models.CharField(max_length=100,blank=True)
    is_certified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'