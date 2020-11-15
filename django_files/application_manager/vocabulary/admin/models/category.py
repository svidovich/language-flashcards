from django.contrib import admin


class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "slug",
        "is_active"
    ]

    ordering = ["name"]

    list_display = [
        "name",
        "slug",
        "isActive"
    ]

    readonly_fields = ['id']
    list_per_page = 30

    def name(self, obj):
        return obj.name
    name.short_description = "Category Name"

    def slug(self, obj):
        return obj.slug
    slug.short_description = "Category Slug"

    def isActive(self, obj):
        return obj.is_active
    isActive.short_description = "Is active"

    def has_add_permission(self, request, obj=None):
        return True

    def has_edit_permission(self, request, obj=None):
        return True
