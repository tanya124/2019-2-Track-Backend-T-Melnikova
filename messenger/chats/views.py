from django.http import JsonResponse
from django.http import HttpResponseNotAllowed


def chat_list(request):
    if request.method == 'GET':
        return JsonResponse({'chat' : 'list'})
    else:
        return HttpResponseNotAllowed(['GET'])


def contacts_list(request):
    if request.method == 'GET':
        return JsonResponse({'contacts' : 'list'})
    else:
        return HttpResponseNotAllowed(['GET'])


def chat_page(request):
    if request.method == 'GET':
        id = request.GET.get("id", 1)
        return JsonResponse({'chat' : id})
    else:
        return HttpResponseNotAllowed(['GET'])