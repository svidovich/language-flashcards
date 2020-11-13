import uuid
from django.db import models


class Words(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    language = models.TextField()
    english_version = models.TextField()
    translated_version = models.TextField()
    definition = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "words"
