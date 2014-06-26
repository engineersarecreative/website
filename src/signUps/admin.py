from django.contrib import admin
from .models import signUp

# Register your models here.
class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = signUp
		
admin.site.register(signUp,SignUpAdmin)
