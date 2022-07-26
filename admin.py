from django.contrib import admin

from gbc.models import   Cart, man, product , woman , body ,cosmetic ,accesory , offers

# Register your models here.

class productadmin(admin.ModelAdmin):
    list_display=['name','price','qty']
    list_filter=['name','price','qty']

admin.site.register(product,productadmin)
admin.site.register(man)
admin.site.register(woman)
admin.site.register(body)
admin.site.register(cosmetic)
admin.site.register(accesory)
admin.site.register(offers)
admin.site.register(Cart)