import os
import uuid
from django.db import models
from taggit_autosuggest.managers import TaggableManager
from django_summernote.models import AbstractAttachment
from django_summernote.utils import get_attachment_storage


def path_file_name(instance, filename):
    filename = "_".join(filter(None, ('audiotop', instance.slug, filename)))
    return os.path.join('projects', instance.slug, filename)


def path_attachment_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % ("audiotop", uuid.uuid4(), ext)
    return os.path.join("projects", "attachment", filename)


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=False)
    slug = models.SlugField(max_length=200, null=True, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, null=False, blank=False)
    address = models.CharField(
        max_length=200, null=True, blank=True, default="")
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to=path_file_name, null=True)
    category = models.ManyToManyField(
        Category, related_name='categories', blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)


class Image(AbstractAttachment):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    file = models.FileField(upload_to=path_attachment_file_name,
                            storage=get_attachment_storage())
