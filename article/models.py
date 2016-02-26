# -*-coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    
    

    def __str__(self):
        return self.title

    class meta:
        ordering = ['-pub_date']