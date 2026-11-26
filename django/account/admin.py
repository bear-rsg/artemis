from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


title = 'ARTEMIS'
admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = ''


class UserAdmin(UserAdmin):
    """
    Customise the admin interface: User
    """

    model = User
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined', 'last_login']
    search_fields = ['username', 'first_name', 'last_name', 'email']
    list_filter = ['is_active',]
    readonly_fields = ['date_joined', 'last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'password1',
                    'password2',
                    'groups',
                ),
            },
        ),
    )
    fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'first_name',
                    'last_name',
                    'password',
                    'is_active',
                    'groups',
                    'date_joined',
                    'last_login',
                ),
            },
        ),
    )

    def has_delete_permission(self, request, obj=None):
        # Nobody can delete users via dashboard (mark them as inactive to prevent login)
        return False


# Register
admin.site.register(User, UserAdmin)
