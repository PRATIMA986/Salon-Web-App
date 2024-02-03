from django.contrib import admin
from detailsform.models import details

class detailsAdmin(admin.ModelAdmin):
    list_display=('name','email','password','confirmpassword','mobileno','city','state','pincode','cname','occupation','yearofexperience')

admin.site.register(details,detailsAdmin)
# Register your models here.
