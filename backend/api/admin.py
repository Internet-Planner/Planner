from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Register your models here.
# admin.site.register(Event)
# admin.site.register(Video)
# admin.site.register(Planning)


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "email",
        "first_name",
        "last_name",
        "nick_name",
        "role",
        "is_staff",
        "is_active",
    ]
    list_display_links = ["email"]
    list_filter = [
        "role",
        "is_staff",
        "is_active",
    ]
    search_fields = ["email", "first_name", "last_name", "nick_name"]
    fieldsets = (
        (
            "Login Credentials",
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                )
            },
        ),
        (
            "Permissions and Groups",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {"fields": ("created_at", "last_login")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "role",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(User, UserAdmin)
