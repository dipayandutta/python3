from django.db import models

# Create your models here.
class Blog(models.Model):
	title 		= models.CharField(max_length=100)
	pub_date	= models.DateTimeField()
	body		= models.TextField()
	image		= models.ImageField(upload_to='images/')
	at_a_glance = models.CharField(max_length=100,default='blog summary')

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')