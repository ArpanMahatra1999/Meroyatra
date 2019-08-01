from django.contrib.auth.models import Permission, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Blog(models.Model):
	title   	= models.CharField(max_length=200)
	blog_type  		= models.CharField(max_length=100)
	description  		= models.TextField()
	blog_image  = models.FileField() 

	def __str__(self):
		return self.title

class Myrating(models.Model):
	user   	= models.ForeignKey(User,on_delete=models.CASCADE) 
	blog 	= models.ForeignKey(Blog,on_delete=models.CASCADE)
	rating 	= models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(0)])
		