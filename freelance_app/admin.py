from django.contrib import admin

# Register your models here.

#
# from django.contrib import admin
# from freelance_app.models import MyUser
#
#
# @admin.register(MyUser)
# class MyUserAdmin(admin.ModelAdmin):
#     list_display = "id", "username", "first_name", "last_name"

from .models import *

admin.site.register(Customer)
admin.site.register(Executor)
admin.site.register(Task)
admin.site.register(Message)
admin.site.register(Support)
