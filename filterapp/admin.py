from django.contrib import admin
from .models import FILE
# Register your models here.
class Adminclass(admin.ModelAdmin):
    list_display = ['Product_Name','Product_URL','Reviews','Review_Count','Price','Image_URL','Category','Sub_Category']
admin.site.register(FILE,Adminclass)
