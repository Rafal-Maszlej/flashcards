from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account, CustomUser


class AccountAdmin(admin.ModelAdmin):
    class Meta:
        model = Account


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Account, AccountAdmin)
