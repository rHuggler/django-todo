from django.db import models
from django.utils.text import Truncator

class Todo(models.Model):
    text = models.CharField(max_length=50, blank=False)
    status = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return Truncator(self.message).chars(20)
