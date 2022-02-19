from django.contrib import admin
from .models import Member
from . import models
# Register your models here.

admin.site.register(Member)
admin.site.register(models.Emoticon)
admin.site.register(models.Likes)
admin.site.register(models.Sell)