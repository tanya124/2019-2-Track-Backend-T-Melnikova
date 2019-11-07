from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotAllowed

def start_page(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')
    else:
        return HttpResponseNotAllowed(['GET'])

def profile(request):
    if request.method == 'GET':
        return JsonResponse({'my' : 'profile'})
    else:
        return HttpResponseNotAllowed(['GET'])
