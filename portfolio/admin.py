from django.contrib import admin
from .models import Home,TextHome,About,Contact,Work

class HomeAdmin(admin.ModelAdmin):
    list_display = ('topic',)
    list_per_page=10
    search_fields=('topic','information',)
# Register your models here.
admin.site.register(Home,HomeAdmin)
admin.site.register(TextHome)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Work)
    
    