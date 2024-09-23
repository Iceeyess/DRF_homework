from django.contrib import admin

from users.models import User

# Register your models here.
admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', )
    list_filter = ('first_name', 'last_name', 'email')
    search_fields = ('email', 'last_name', 'first_name', )