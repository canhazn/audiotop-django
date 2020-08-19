from django.shortcuts import render, get_object_or_404
from lighting import models, serializers
from html2text import html2text

TEMPLATE_LIST = 'lighting_list.html'
TEMPLATE_DETAIL = 'lighting_detail.html'


def productList(request):

    product_queryset = models.Produkt.objects.all()

    product_serializer = serializers.ProduktSerializer(
        product_queryset, many=True)

    context = {
        "app_url": "lighting",
        "products": product_serializer.data
    }

    return render(request, TEMPLATE_LIST, context)


def productDetail(request, slug):
    product = get_object_or_404(models.Produkt, slug=slug)

    product.description = html2text(product.content)
    tags = product.tags.all()
    product.titleTag = product.title
    for tag in tags:
        if tag:
            product.titleTag += ' | %s' % (tag.name)

    related_product = product.tags.similar_objects()[:4]
    
    context = {
        "app_url": "lighting",
        "product": product,
        "related_product": related_product
    }
    return render(request, TEMPLATE_DETAIL, context)
