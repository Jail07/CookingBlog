from django.contrib import admin

from main.models import *


class ImageInlaneAdmin(admin.TabularInline):
    model = Image
    fields = ('image',)
    max_num = 5


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInlaneAdmin,]


admin.site.register(Category)



