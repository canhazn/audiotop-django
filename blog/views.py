from django.shortcuts import render, get_object_or_404
from blog import models, serializers
from html2text import html2text


TEMPLATE_LIST = 'blog_list.html'
TEMPLATE_DETAIL = 'blog_detail.html'


def blogList(request):

    blog_queryset = models.Blog.objects.all()
    blog_serializer = serializers.BlogSerializer(
        blog_queryset, many=True)    
    context = {
    "app_url": "blog",
        "blogs": blog_serializer.data
    }

    return render(request, TEMPLATE_LIST, context)


def blogDetail(request, slug):
    blog = get_object_or_404(models.Blog, slug=slug)

    blog.description = html2text(blog.content)   
    tags = blog.tags.all()
    blog.titleTag = blog.title
    for tag in tags:
        if tag: 
            blog.titleTag += ' | %s' % (tag.name)     


    related_blog = blog.tags.similar_objects()[:4]

    context = {
    "app_url": "blog",
        "blog": blog,        
        "related_blog": related_blog
    }
    return render(request, TEMPLATE_DETAIL, context)
