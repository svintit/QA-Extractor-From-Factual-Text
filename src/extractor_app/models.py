from django.db import models
from django.conf import settings


class Post(models.Model):
    post = models.TextField()


class Questions(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    inputted_text = models.TextField(blank=True, null=True)

    list_title = models.CharField(max_length=256, blank=True, null=True)

    qa_list = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'list_title']


class UniqueSession(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    sessionid = models.CharField(max_length=25, blank=True, null=True)

    qa_list = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    inputted_text = models.TextField(blank=True, null=True)

    list_title = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        unique_together = ['user', 'sessionid']
