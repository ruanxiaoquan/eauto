# -*- coding=utf-8 -*-
import sys
sys.path.append("..")
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from eauto.gpio_service import service


def home(res):
    ctx = {}
    ctx['hello'] = 'Hello World!'
    return render(res, "home.html", ctx)


@csrf_exempt
def go(res):
    type = res.POST.get("type")
    result = {}
    if type == 'default':
        result["direction"] = '向前'
        service.default()
    elif type == 'reverse':
        result["direction"] = '向后'
        service.reverse()
    else:
        result["direction"] = '停止'
        service.stop()
    return JsonResponse(result)
