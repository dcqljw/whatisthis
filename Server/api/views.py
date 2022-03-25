from django.core.cache import cache
from django.http import JsonResponse

from api.Utils import create_one_url


def index(request):
    return JsonResponse({"code": "2000", "msg": "ok"})


def short_url(request):
    context = {}
    return JsonResponse(context)


def one_url(request):
    xby = request.GET.get("xby")
    context = {}
    if cache.get(xby) is not None:
        context = {"msg": cache.get(xby)}
        cache.delete(xby)
    return JsonResponse(context)


def create_article(request):
    text = request.POST.get("text")
    date = request.POST.get("date")
    sign = create_one_url(date)
    cache.set(sign, text)
    context = {sign: text}
    return JsonResponse(context)
