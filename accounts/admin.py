from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Account


class CustomUserAdmin(UserAdmin):
    """
    custom admin panel for user management that change form and add email instead username.
    """

    model = User
    list_display = ("email", "is_superuser", "is_staff", "is_active", "is_verified")
    list_filter = ("email", "is_superuser", "is_staff", "is_active", "is_verified")
    search_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": ("is_superuser", "is_staff", "is_active", "is_verified"),
            },
        ),
        (
            "group permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                    "is_verified",
                ),
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)


class AccountManager(admin.ModelAdmin):
    """
    this class is for manage profile
    """

    model = Account
    list_display = ("user", "first_name", "last_name", "created_date", "id")
    search_fields = ("user", "first_name", "last_name")
    ordering = ("created_date",)


admin.site.register(Account, AccountManager)