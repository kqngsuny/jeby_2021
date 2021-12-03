
from django.contrib import admin
from .models import Keyword, Site

# admin.site.register(Keyword)


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    pass


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    pass