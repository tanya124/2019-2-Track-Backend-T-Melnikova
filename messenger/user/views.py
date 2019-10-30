from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseBadRequest

def start_page(request):
    if request.method == 'GET':
        return render(request, 'main_page.html')
    else:
        return HttpResponseBadRequest()

def profile(request):
    if request.method == 'GET':
        return JsonResponse({'my' : 'profile'})
    else:
        return HttpResponseBadRequest()