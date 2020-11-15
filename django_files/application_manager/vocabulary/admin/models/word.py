from django.contrib import admin


class WordAdmin(admin.ModelAdmin):
    search_fields = [
        "english_version",
        "translated_version",
        "language",
        "category"
    ]

    ordering = ["english_version"]

    list_display = [
        "englishVersion",
        "translatedVersion",
        "language",
        "category",
        "definition"
    ]

    readonly_fields = ['id']
    list_per_page = 30

    def englishVersion(self, obj):
        return obj.english_version
    englishVersion.short_description = "English Version"

    def translatedVersion(self, obj):
        return obj.translated_version
    translatedVersion.short_description = "Translated Version"

    def language(self, obj):
        return obj.language
    language.short_description = "Language"

    def category(self, obj):
        return obj.category
    category.short_description = "Word Categories"

    def definition(self, obj):
        return obj.definition
    category.short_description = "Word Definition"

    def has_add_permission(self, request, obj=None):
        return True

    def has_edit_permission(self, request, obj=None):
        return True