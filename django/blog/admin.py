from django.contrib import admin
from . import models


def publish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to published
    """
    queryset.update(published=True)


publish.short_description = "Publish selected items (will appear on main site)"


def unpublish(modeladmin, request, queryset):
    """
    Sets all selected items in queryset to not published
    """
    queryset.update(published=False)


unpublish.short_description = "Unpublish selected items (will not appear on main site)"


class BlogAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of Blog in the Django admin
    """
    list_display = ('id', 'title', 'date', 'published',)
    list_filter = ('published',)
    search_fields = ('title', 'subtitle', 'article')
    actions = (publish, unpublish)


admin.site.register(models.Blog, BlogAdminView)


class BlogImageAdminView(admin.ModelAdmin):
    """
    Customise the content of the list of BlogImage in the Django admin
    """
    list_display = ('id', 'image_url', 'image_description', 'date')
    search_fields = ('image_description',)


admin.site.register(models.BlogImage, BlogImageAdminView)
