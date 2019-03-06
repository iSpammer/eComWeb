from __future__ import unicode_literals

from django.db import models


#this model is used to store user data
#text field
# Create your models here.
class profile(models.Model):
	name= models.CharField(max_length=120)
	description = models.TextField(default = 'description default text')

	def __unicode__(self):
		return self.name #display name