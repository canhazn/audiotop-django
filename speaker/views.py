from django.shortcuts import render
from speaker import models


TEMPLATE_LIST = 'speaker_list.html'
TEMPLATE_DETAIL = 'speaker_detail.html'


def productList(request):
    return render(request, TEMPLATE_LIST)


def productDetail(request, pk):
    return render(request, TEMPLATE_DETAIL)
