import os
import uuid
from taggit_autosuggest.managers import TaggableManager
from django.db import models
from django_summernote.models import AbstractAttachment
from django_summernote.utils import get_attachment_storage


def path_file_name(instance, filename):
    newName = "_".join(filter(None, (instance.slug, filename)))
    return "%s/%s/%s" % ('speakers', instance.slug, newName)


def path_attachment_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % ("audiotop", uuid.uuid4(), ext)
    return os.path.join("speakers", "attachment", filename)


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    slug = models.SlugField(max_length=200, null=True, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Product(models.Model):
    class Meta:
        ordering = ['index']
    title = models.CharField(max_length=200, null=False, blank=False)
    index = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to=path_file_name, null=True)
    tags = TaggableManager()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='category', null=True, blank=True, default="")

    def __str__(self):
        return str(self.title)


class Image(AbstractAttachment):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    file = models.FileField(upload_to=path_attachment_file_name,
                            storage=get_attachment_storage())
