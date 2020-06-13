from django.contrib import admin

from .models import User, Issue, Comments, Company

@admin.register(Issue)
class IssueModelAdmin(admin.ModelAdmin):
    pass

@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Comments)
class CommentsModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Company)
class CompanyModelAdmin(admin.ModelAdmin):
    pass