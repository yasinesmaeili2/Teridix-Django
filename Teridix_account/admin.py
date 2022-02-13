from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin



# add field UserModel for showing


# UserAdmin.fieldsets[4][1] += (
#     'is_active',
#     'is_staff',
#     'is_superuser',
#     'is_auther',
#     'special_user'
#     'groups',
#     'user_permissions',
# )


UserAdmin.fieldsets += (
    (None,{'fields':('is_auther',)}),
)

UserAdmin.list_display += ('is_auther',)

admin.site.register(User,UserAdmin)