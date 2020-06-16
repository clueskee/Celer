import uuid

from tinymce import HTMLField

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse

from app.choices import PRIORITY, STATUS


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=32, null=True)


class User(AbstractUser):
    company = models.ForeignKey(Company, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=32, null=True)


class Issue(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=254, null=False)
    description = HTMLField('Description')
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(null=True)
    priority = models.IntegerField(choices=PRIORITY, default=1)
    status = models.IntegerField(choices=STATUS, default=1)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    # TODO: Sprawdź czy to najlepszy sposób:
    def get_absolute_url(self):
        # return f"{self.id}"
        return reverse('app:show_issue', args=[self.id])

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    content = HTMLField('Content')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='comments')
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['creation_date']

    def __str__(self):
        return '{} [{}]'.format(self.content, self.user)