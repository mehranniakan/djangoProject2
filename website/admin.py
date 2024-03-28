from django.contrib import admin

# Register your models here.
from website.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'Created_date'
    list_display = ('Name', 'Email', 'Created_date')
    list_filter = ('Email',)
    search_fields = ('Name', 'Message')
