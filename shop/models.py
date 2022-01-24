
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from django.utils import timezone
#from django_google_maps import fields as map_fields

# Create your models here.


#all the categories 
class Categories(models.Model):
    category_name = models.CharField(max_length=80)
    category_description = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.category_name







#all the actual items under the categories
class Category_item(models.Model):
    category_item_id = models.ForeignKey(Categories, on_delete=models.CASCADE)







#what a post will have as information in the database
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50,default='Item for sale')
    price = models.CharField(max_length=200)
    description = models.TextField(max_length=800)
    published_date = models.DateTimeField("date published",default= timezone.now)
    is_active = models.BooleanField(default=True)
    longitude = models.FloatField(blank = False, null = False, default=0) # longitude for the google map api 
    latitude = models.FloatField(blank = False, null = False, default=0) # google map api implementation
    

    def get_image_filename(instance, filename):
        title = instance.post.title
        slug = slugify(title)
        return "post_images/%s-%s" % (slug, filename)  

    def __str__(self):
        return self.title


#Images that come with the post
class Post_image(models.Model):
    ad_id = models.ForeignKey(Post,on_delete=models.CASCADE)
    pic_1 = models.ImageField(upload_to='static/images/posts',blank=True)
    pic_2 = models.ImageField(upload_to='static/images/posts',blank=True)
    pic_3 = models.ImageField(upload_to='static/images/posts',blank=True)
    pic_4 = models.ImageField(upload_to='static/images/posts',blank=True)
    pic_5 = models.ImageField(upload_to='static/images/posts',blank=True)
    pic_6 = models.ImageField(upload_to='static/images/posts',blank=True)

    def __str__(self):
        return 'images'
    
        


#class Images(models.Model):
 #   post = models.ForeignKey(Post, default=None, on_delete= models.CASCADE)
  #  image = models.ImageField(upload_to='static/static_dirs/images',verbose_name='Image')