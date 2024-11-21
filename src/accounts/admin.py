from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User

class UserAdmin(BaseUserAdmin):
    # user一覧の表示を変える
    list_display = (
        "account_id",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    list_filter = (
        "is_superuser",
        "is_active",
    )
    ordering = ("email",)
    filter_horizontal = ()

    # user追加のフィールドを指定
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

    # 編集ページのフィールドを指定
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('権限', {'fields': ('is_staff','is_superuser',)}),
    )


admin.site.register(User, UserAdmin)  # Userモデルを登録
admin.site.unregister(Group)  # Groupモデルは不要のため非表示にします