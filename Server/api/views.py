import re

from django.core.cache import cache
from django.http import JsonResponse, HttpResponseRedirect
from django.conf import settings
from rest_framework.decorators import api_view

from api.Utils import create_one_url

host_domain_name = settings.HOST_DOMAIN_NAME
client_name = settings.CLIENT_NAME


@api_view(["GET"])
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


@api_view(["POST"])
def create_article(request):
    """
    创建文章
    :param request:
    :return: 文章链接
    """
    text = request.data.get("text")
    date = request.data.get("date")
    if (text and date) is not None:
        sign = create_one_url(date)
        try:
            cache.set(sign, text)
        except Exception:
            return JsonResponse({"msg": "error"})
        # context = {sign: text}
        context = {
            "code": "1000",
            "href": f"http://{client_name}/xby?xby={sign}"
        }
        return JsonResponse(context)
    else:
        return JsonResponse({"msg": "error"})


@api_view(["POST", "GET"])
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
            context = {"url": f"http://{host_domain_name}/d/{key}"}
        else:
            href = f"http://{href}"
            cache.set(key, href)
            context = {"url": f"http://{host_domain_name}/d/{key}"}
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
