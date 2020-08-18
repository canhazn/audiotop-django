from django.shortcuts import render, get_object_or_404
from speaker import models, serializers

TEMPLATE_LIST = 'speaker_list.html'
TEMPLATE_DETAIL = 'speaker_detail.html'


def productList(request):

    product_queryset = models.Product.objects.all()

    product_serializer = serializers.ProductSerializer(
        product_queryset, many=True)

    context = {
        "app_url": "speaker",
        "products": product_serializer.data
    }

    return render(request, TEMPLATE_LIST, context)


def productDetail(request, slug):
    product = get_object_or_404(models.Product, slug=slug)
    related_product = product.tags.similar_objects()[:4]
    print(related_product)
    context = {
        "app_url": "speaker",
        "product": product,        
        "related_product": related_product
    }
    return render(request, TEMPLATE_DETAIL, context)
