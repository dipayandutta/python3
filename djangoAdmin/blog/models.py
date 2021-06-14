from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name 


class post(models.Model):

	options = (
		('draft','Draft'),
		('published','Published'),
		)

	category = models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
	title = models.CharField(max_length=200,null=True)
	excerpt = models.TextField(null=True)
	slug = models.SlugField(max_length=250,unique_for_date='publish',null=True)
	author = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
	publish = models.DateTimeField(default=timezone.now)
	content = models.TextField(null=True)
	status = models.CharField(max_length=10,choices=options,default='draft')

	
	def __str__(self):
		return self.title