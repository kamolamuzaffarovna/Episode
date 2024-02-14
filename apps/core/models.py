from django.db import models
from apps.blog.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=221)
    email = models.EmailField(max_length=221, null=True, blank=True)
    subject = models.CharField(max_length=221)
    message = models.TextField()

    def __str__(self):
        return self.name
