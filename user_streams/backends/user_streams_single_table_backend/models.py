from django.conf import settings
from django.db import models

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class StreamItem(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name='+')
    content = models.TextField()
    created_at = models.DateTimeField()

    class Meta:
        ordering = ['-created_at']
