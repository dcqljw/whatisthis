import re

from django.core.cache import cache
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.decorators import api_view

from api.Utils import create_one_url


def one_url(request):
    """
    一次性url
    :param request:
    :return: 文章内容
    """
    xby = request.GET.get("xby")
    if cache.get(xby) is not None:
        context = {"msg": cache.get(xby)}
        cache.delete(xby)
        return JsonResponse(context)
    else:
        return JsonResponse({})


def create_article(request):
    """
    创建文章
    :param request:
    :return: 文章链接
    """
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
    """
    转换为短链接
    :param request:
    :return: JSON
    """
    href = request.POST.get('href')
    key = create_one_url(href)[2:10]
    pattern = re.compile(r"[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?")
    if pattern.search(href):
        if href[:4] == "http":
            cache.set(key, href)
            context = {"url": f"http://127.0.0.1:8000/d/{key}"}
        else:
            href = f"http://{href}"
            cache.set(key, href)
            context = {"url": f"http://127.0.0.1:8000/d/{key}"}
        return JsonResponse(context)
    else:
        return JsonResponse({})


@api_view(["GET"])
def short_redirect(request, short):
    """
    重定向目标链接
    :param request:
    :param short:
    :return: JSON
    """
    href = cache.get(short)
    if href is not None:
        return HttpResponseRedirect(href)
    else:
        return JsonResponse({"msg": "not found"})
