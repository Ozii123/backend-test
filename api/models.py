from operator import mod
from statistics import mode
from django.db import models
import uuid


# Create your models here.
class Section(models.Model):
    id =  models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    created_at   = models.DateTimeField(auto_now=True)
    last_updated  =  models.DateTimeField(blank=True,null=True)
    title      = models.TextField()
    body        = models.TextField()
    parent_section  = models.ForeignKey('self', blank=True, null=True, on_delete=models.NOT_PROVIDED)