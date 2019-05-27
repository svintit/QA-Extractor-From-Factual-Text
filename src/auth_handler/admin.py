from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserProfile


class UserAdmin(BaseUserAdmin):
    list_display = (
        'name',
        'email',
        'org',
        'confirmed_email',
        'admin',
        'staff',
        'active'
       )
    list_filter = ('org', 'confirmed_email', 'admin', 'staff', 'active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin',)}),
    )

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )
    search_fields = ('email', 'name', 'org')
    ordering = ('email', 'name', 'org')
    filter_horizontal = ()


admin.site.register(UserProfile, UserAdmin)
admin.site.unregister(Group)
