from django.contrib import admin
from .models import Post, Category


@admin.action(description="Mark selected posts as published")
def mark_selected_posts_as_published(modeladmin, request, queryset):
    queryset.update(published=True)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "published",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "published",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "body",
    )

    list_editable = (
        "published",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    actions = [mark_selected_posts_as_published]