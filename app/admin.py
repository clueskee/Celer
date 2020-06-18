from django.contrib import admin

from .models import Issue, Comments, Company

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
