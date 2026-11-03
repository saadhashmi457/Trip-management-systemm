from django.contrib import admin
from services.models import Services


# Register your models here.
class serviceadmin(admin.ModelAdmin):
    list_display=('Services_title','Services_detail')
    
    
admin.site.register(Services,serviceadmin)
