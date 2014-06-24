from django.db import models
from django.utils.encoding import smart_unicode
from django import forms

# Create your models here.
class signUp(models.Model):
	first_name = models.CharField(max_length = 120,null=True,blank=True)
	last_name = models.CharField(max_length = 120,null=True,blank=True)
	email = models.EmailField()
	password = models.CharField(max_length = 120)
	
	def __unicode__(self):
		return smart_unicode(self.email)