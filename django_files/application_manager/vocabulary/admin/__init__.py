from django.contrib import admin
from django.conf import settings
from django.contrib.sites.models import Site

from vocabulary.models import Words, Category
from vocabulary.admin.models import WordAdmin, CategoryAdmin

admin.site.site_header = "Language Flashcards Administration! Yay!"

admin.site.unregister(Site)


admin.site.register(Words, WordAdmin)
admin.site.register(Category, CategoryAdmin)
