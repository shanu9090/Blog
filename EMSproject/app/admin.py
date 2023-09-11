from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.AdminDB)
admin.site.register(models.UserDB)
admin.site.register(models.EnquiryDB)
