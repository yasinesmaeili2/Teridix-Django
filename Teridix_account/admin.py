from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin



# add field UserModel for showing
UserAdmin.fieldsets += (
    (None,{'fields':('is_auther','image')}),
)
UserAdmin.list_display += ('is_auther',)
admin.site.register(User,UserAdmin)
