from django.db import models


class UserAnswer(models.Model):
    username = models.CharField(max_length=256, blank=True, null=True)

    inputted_text = models.TextField(blank=True, null=True)

    qalist = models.TextField()

    created = models.DateTimeField(auto_now_add=True)

    sessionid = models.CharField(max_length=25, blank=True, null=True)

    creationuser = models.CharField(max_length=25, blank=True, null=True)

    averagegrade = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ['username', 'sessionid', 'created']
