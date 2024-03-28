from django.contrib import admin

# Register your models here.

from blog.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Name',)
    list_filter = ('Name',)
    search_fields = ('Name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'Created_date'
    list_display = ('Title', 'Author', 'Status', 'Created_date')
    list_filter = ('Title', 'Status', 'Author')
    search_fields = ('Title', 'Content')
