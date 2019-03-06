from django.contrib import admin

# Register your models here.
#import profile model to admin.py
from .models import profile

#to make profile admin managable
class profileAdmin(admin.ModelAdmin):
	class Meta:
		model = profile
admin.site.register(profile, profileAdmin)