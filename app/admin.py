from django.contrib import admin

from .models import Issue, Comments, Company
from django.contrib.auth.admin import UserAdmin

from app.forms import CustomUserCreationForm, CustomUserChangeForm
from app.models import CustomUser

@admin.register(Issue)
class IssueModelAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'date_start',
                    'date_end',
                    'priority',
                    'status',
                    'active',
                    'user')

@admin.register(Comments)
class CommentsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    pass


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'company')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)