from django.contrib import admin

from .models import Women, Category


@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


# admin.site.register(Women, WomenAdmin)
admin.site.register(Category)
