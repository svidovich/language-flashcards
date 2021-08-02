import uuid
from django.db import models


class Languages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        db_table = "languages"
        app_label = "vocabulary"
        verbose_name_plural = "Languages"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    related_words = models.ManyToManyField('Words')

    class Meta:
        db_table = "categories"
        app_label = "vocabulary"
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Words(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    language = models.ForeignKey(Languages, on_delete=models.PROTECT)
    english_version = models.TextField()
    translated_version = models.TextField()
    definition = models.TextField(blank=True, null=True)
    word_categories = models.ManyToManyField('Category')

    class Meta:
        db_table = "words"
        app_label = "vocabulary"
        verbose_name_plural = 'Words'

    def __str__(self):
        return self.english_version
