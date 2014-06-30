from django.db import models
from django.utils.encoding import smart_unicode
from django import forms

# Create your models here.
class signUp(models.Model):
	first_name = models.CharField(max_length = 120,null=True,blank=True)
	last_name = models.CharField(max_length = 120,null=True,blank=True)
	email = models.EmailField()
	username = models.CharField(max_length = 120)
	password = models.CharField(max_length = 120)
	
	def __unicode__(self):
		return smart_unicode(self.email)

#NEED TO GET RID OF ALL MODELS EVENTUALLY, NO LONGER REQUIRED