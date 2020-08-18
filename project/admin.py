from project import models
from django.contrib import admin
from django.utils.html import format_html
from django.shortcuts import get_object_or_404

# Summer note
from django_summernote.admin import SummernoteModelAdmin, AttachmentAdmin

# get images from content
from bs4 import BeautifulSoup

# change django summernote model
from django.conf import settings as django_settings
from audiotop_django import settings


def change_sumernote_attchment_model():
    ATTACHMENT_MODEL = "project.Image"
    setattr(django_settings, 'SUMMERNOTE_CONFIG', {
        "attachment_model": ATTACHMENT_MODEL
    })


def get_img_urls(html_content, obj):
    """
    Return array of url of images attachment of main model
    """
    img_urls = []

    soup = BeautifulSoup(html_content, 'html.parser')
    imgs = soup.find_all('img')

    for image in imgs:
        if image['src'].find("audiotop") != -1:
            img_urls.append(image['src'])
            # Remove string /media/
            print(image['src'][7:])
            imageObject = models.Image.objects.get(file=image['src'][7:])
            try:
                projectObject = models.Project.objects.get(slug=obj.slug)
                imageObject.project = projectObject
            except models.Project.DoesNotExist:
                print("This project is note exsits: %s", str(obj.slug))
                # projectObject = get_object_or_404(models.Project, slug = obj.slug)
                # if projectObject:
        print(type(obj).__name__)
        imageObject.save()
        print(imageObject)
    return img_urls


class ImageAdmin(AttachmentAdmin):
    """
    Inherit django_summernote attachmentadmin and add custom display field
    """
    list_display = ['name', 'file', 'uploaded', 'get_foreignkey']

    def get_foreignkey(self, obj):
        if obj.project:
            return obj.project
        return format_html("<span style='color: red;'>...</span>")

    get_foreignkey.short_description = "Project"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('slug', 'title', 'get_tags', 'get_thumb')
    prepopulated_fields = {'slug': ('title', )}

    # Change django sumernote attachment object every time init form
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=None, change=False, **kwargs)
        change_sumernote_attchment_model()
        return form

    def get_tags(self, obj):
        return ",".join([tag.name for tag in obj.tags.all()])
    get_tags.short_description = "TAGS"

    def get_thumb(self, obj):
        return format_html('<img style="width:200px;" src="{}"/>'.format(obj.thumb.url))
    get_thumb.short_description = "Thumb"

    def save_model(self, request, obj, form, change):
        html_content = obj.content
        get_img_urls(html_content, obj)
        super().save_model(request, obj, form, change)


admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Project, ProjectAdmin)
