from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "avatar",
        "phone_number",
        "country",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = ("is_active", "email", "is_staff", "country")
    search_fields = ("email",)
