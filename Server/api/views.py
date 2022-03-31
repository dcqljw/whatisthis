from django.core.cache import cache
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.decorators import api_view

from api.Utils import create_one_url


def one_url(request):
    xby = request.GET.get("xby")
    context = {}
    print(xby)
    if cache.get(xby) is not None:
        context = {"msg": cache.get(xby)}
        cache.delete(xby)
    return JsonResponse(context)


def create_article(request):
    text = request.POST.get("text")
    date = request.POST.get("date")
    if (text and date) is not None:
        sign = create_one_url(date)
        cache.set(sign, text)
        # context = {sign: text}
        context = {
            "code": "1000",
            "href": f"http://127.0.0.1:8000/xby?xby={sign}"
        }
        return JsonResponse(context)
    else:
        return JsonResponse({"msg": "error"})


@api_view(["POST"])
def short_link(request):
    # href = request.GET.get('href')
    cache.set("1", "https://www.baidu.com")
    return JsonResponse({"code": "1000"})


@api_view(["GET"])
def test(request, short):
    href = cache.get(short)
    return HttpResponseRedirect(href)
