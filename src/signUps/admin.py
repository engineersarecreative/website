from django.contrib import admin
from .models import signUp

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = signUp
# Sets up signUp class with admin site, will need to remove SignUpAdmin in the future
admin.site.register(signUp,SignUpAdmin)
 