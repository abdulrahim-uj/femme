from django.contrib import admin
from web.models import RegistrationClass


# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'dob', 'education', 'message')


admin.site.register(RegistrationClass, RegistrationAdmin)
