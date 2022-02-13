from django.contrib import admin
from django.contrib.auth.models import Group

from app.internal.admin.admin_user import UserAdmin
from app.internal.models.user import User

admin.site.site_title = "Backend course"
admin.site.site_header = "Backend course"
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
