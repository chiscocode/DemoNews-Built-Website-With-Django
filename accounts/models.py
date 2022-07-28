from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.db.models import Count
# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=255,null=True)
    slug=models.SlugField(max_length=255,null=True)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class Post(models.Model):
    category=models.ForeignKey(Category, related_name='posts', on_delete= models.CASCADE)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation', default='')
    photo=models.ImageField(blank=True,null=False)
    title=models.CharField(max_length=255, null=True)
    slug=models.SlugField(max_length=255, null=True)
    description=RichTextUploadingField(blank=True,null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    viewers = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='posts',editable=False)
    date_added= models.DateTimeField(auto_now_add=True)   
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

class MainPost(models.Model):
    category=models.ForeignKey(Category, related_name='mainposts', on_delete= models.CASCADE)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation',default='')
    photo=models.ImageField(blank=True,null=False)
    title=models.CharField(max_length=255, null=True)
    slug=models.SlugField(max_length=255, null=True)
    description=RichTextUploadingField(blank=True,null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date_added= models.DateTimeField(auto_now_add=True)   
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
    
class MainComment(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    body=models.TextField()
    post=models.ForeignKey(MainPost, on_delete=models.CASCADE, related_name='maincomments',null=False, default='')
    date_added= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name   



class FeaturedPost(models.Model):
    category=models.ForeignKey(Category, related_name='featuredposts', on_delete= models.CASCADE)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation',default='')
    photo=models.ImageField(blank=True,null=False)
    title=models.CharField(max_length=255, null=True)
    slug=models.SlugField(max_length=255, null=True)
    description=RichTextUploadingField(blank=True,null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date_added= models.DateTimeField(auto_now_add=True)   
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
    
class FeaturedComment(models.Model):
    name=models.CharField(max_length=100,null=False,blank=True)
    body=models.TextField()
    post=models.ForeignKey(FeaturedPost, on_delete=models.CASCADE, related_name='featuredcomments',null=False, default='')
    date_added= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name   

class Comment(models.Model):
    name=models.CharField(max_length=100,null=False,blank=True)
    body=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='commen',null=False, default='')
    date_added= models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.name
        
class Newsletter(models.Model):
    email=models.EmailField(max_length=200,null=True, blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return self.email

class AdvertisementOne(models.Model):
    photo=models.ImageField(blank=True,null=False)
    links=models.CharField(max_length=200,null=False,blank=True)

    def __str__(self):
        return self.links


class AdvertisementThree(models.Model):
    photo=models.ImageField(blank=True,null=False)
    links=models.CharField(max_length=200,null=False,blank=True)

    def __str__(self):
        return self.links


class Contact(models.Model):
    email=models.EmailField(max_length=100, blank=True, null=False)
    subject=models.CharField(max_length=400,blank=True,null=False)
    message=models.TextField(blank=True)
    date_added= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

