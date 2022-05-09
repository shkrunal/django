from django.contrib import admin


from .models import contect, feedback ,cal

# Register your models here.
admin.site.register(feedback)
admin.site.register(contect)
admin.site.register(cal)