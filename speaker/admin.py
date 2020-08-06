from speaker import models
from django.contrib import admin
from django.utils.html import format_html

# Summer note
from django_summernote.admin import SummernoteModelAdmin, AttachmentAdmin

# get images from content
from bs4 import BeautifulSoup

# change django summernote model
from django.conf import settings as django_settings
from audiotop_django import settings


def change_sumernote_attchment_model():
    ATTACHMENT_MODEL = "speaker.Image"
    setattr(django_settings, 'SUMMERNOTE_CONFIG', {
        "attachment_model": ATTACHMENT_MODEL
    })
    print("Changed attchment model", getattr(django_settings, 'SUMMERNOTE_CONFIG', {}))


class ImageAdmin(AttachmentAdmin):
    """
    Inherit django_summernote attachmentadmin and add custom display field
    """
    list_display = ['name', 'file', 'uploaded', 'get_foreignkey']

    def get_foreignkey(self, obj):
        if obj.product:
            return obj.product
        return format_html("<span style='color: red;'>...</span>")

    get_foreignkey.short_description = "Product"


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('slug', 'title', 'get_tags', 'get_thumb')
    prepopulated_fields = {'slug': ('title', )}

    # Change django sumernote attachment object every time init form
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=None, change=False, **kwargs)
        change_sumernote_attchment_model()
        return form

    def get_tags(self, obj):
        return ",".join([tag.title for tag in obj.tags.all()])

    get_tags.short_description = "TAGS"

    def get_thumb(self, obj):
        return format_html('<img style="width:200px;" src="{}"/>'.format(obj.thumb.url))

    get_thumb.short_description = "Thumb"


admin.site.register(models.Image, ImageAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Product, ProductAdmin)
