import os
import uuid
from taggit_autosuggest.managers import TaggableManager
from django.db import models
from django_summernote.models import AbstractAttachment
from django_summernote.utils import get_attachment_storage


def path_file_name(instance, filename):
    newName = "_".join(filter(None, (instance.slug, filename)))
    return "%s/%s/%s" % ('blogs', instance.slug, newName)


def path_attachment_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % ("audiotop", uuid.uuid4(), ext)
    return os.path.join("blogs", "attachment", filename)


class Blog(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to=path_file_name, null=True)
    tags = TaggableManager(blank=True)   

    def __str__(self):
        return str(self.title)


class Image(AbstractAttachment):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="images", null=True, blank=True)
    file = models.FileField(upload_to=path_attachment_file_name,
                            storage=get_attachment_storage())
