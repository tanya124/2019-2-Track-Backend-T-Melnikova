from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseNotAllowed
from django.views.generic import View

def chat_list(request):
    if request.method == 'GET':
        return JsonResponse({'chat' : 'list'})
    else:
        return HttpResponseNotAllowed(request.method)

def chat_details(request):
    if request.method == 'GET':
        chat_id = request.GET.get("id", "no_chat")
        if chat_id == "no_chat":
            raise Http404
        else:
            return JsonResponse({'chat' : chat_id})
    else:
        return HttpResponseNotAllowed(request.method)

def contacts_list(request):
    if request.method == 'POST':
        return JsonResponse({'contacts' : 'list'})
    else:
        return HttpResponseNotAllowed(request.method)

def chat_page(request):
    if request.method == 'GET':
        id = request.GET.get("id", 1)
        return JsonResponse({'chat' : id})
    else:
        return HttpResponseNotAllowed(request.method)