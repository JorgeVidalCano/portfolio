from django.contrib.auth.models import Group
from django.contrib import admin
from .models import *

admin.site.unregister(Group)

class CommonFunctions():
    def has_add_permission(self, request, obj=None):
        # The add button disapear when there is one.
        if self.objects.all().count() == 1:
            return False
        else:
            return True

@admin.register(MetaData)
class MetaAdmin(admin.ModelAdmin):
    list_display = ['metaDescription', 'metaKeywords']
    
    def has_add_permission(self, request, obj=None):
        # The add button disapear when there is one.
        if MetaData.objects.all().count() == 1:
            return False
        else:
            return True

@admin.register(HomeData)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['mainName', 'description']
    
    def has_add_permission(self, request, obj=None):
        # The add button disapear when there is one.
        if HomeData.objects.all().count() == 1:
            return False
        else:
            return True

@admin.register(AboutData)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    
    def has_add_permission(self, request, obj=None):
        # The add button disapear when there is one.
        if AboutData.objects.all().count() == 1:
            return False
        else:
            return True

@admin.register(SkillData)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill']
    
@admin.register(DetailsData)
class DetailsDataAdmin(admin.ModelAdmin):
    list_display = ['detail']


class DetailListAdmin(admin.StackedInline):
    list_display =("detail")
    model = DetailsData
    

@admin.register(ResumeData)
class ResumeData(admin.ModelAdmin):
    inlines = [DetailListAdmin]
    list_display = ['name', 'start', 'end', 'resume', 'company', 'language']
    