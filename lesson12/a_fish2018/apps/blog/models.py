# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# Create your models here.

from django.db import models
from dashboard.models import UserProfile
class Note(models.Model):
    user = models.ForeignKey(UserProfile)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()
    def __str__(self):
        return self.title
