from django.shortcuts import render, get_object_or_404
from lighting import models, serializers

TEMPLATE_LIST = 'lighting_list.html'
TEMPLATE_DETAIL = 'lighting_detail.html'


def productList(request):

    product_queryset = models.Produkt.objects.all()

    product_serializer = serializers.ProduktSerializer(
        product_queryset, many=True)

    context = {
        "products": product_serializer.data
    }

    return render(request, TEMPLATE_LIST, context)


def productDetail(request, slug):
    product = get_object_or_404(models.Produkt, slug=slug)
    related_product = product.tags.similar_objects()[:4]
    print(related_product)
    context = {
        "product": product,        
        "related_product": related_product
    }
    return render(request, TEMPLATE_DETAIL, context)
