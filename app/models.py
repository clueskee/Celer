import datetime
import uuid

from django.urls import reverse
from tinymce import HTMLField

from django.db import models
from django.utils import timezone

from app.choices import PRIORITY, STATUS


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256, null=True)
    address = models.CharField(max_length=256, null=True)
    phone = models.CharField(max_length=32, null=True)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, null=True)
    surname = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=32, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Issue(models.Model):
    id = models.IntegerField(primary_key=True)
    issue_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title =  models.CharField(max_length=256, null=False)
    email = models.EmailField(max_length=254, null=False)
    description = HTMLField('Description')
    date_start = models.DateTimeField(default=timezone.now)
    date_end = models.DateTimeField(null=True)
    priority = models.IntegerField(choices=PRIORITY, default=1)
    status = models.IntegerField(choices=STATUS, default=1)
    active = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        # return f"{self.id}"
        return reverse('app:show_issue', args=[str(self.id)])

class Comments(models.Model):
    id = models.IntegerField(primary_key=True)
    content = HTMLField('Content')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)