from django.contrib import admin

from luz.base.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
