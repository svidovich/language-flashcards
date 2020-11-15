import uuid
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class Words(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    language = models.TextField()
    english_version = models.TextField()
    translated_version = models.TextField()
    definition = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)


    class Meta:
        db_table = "words"
