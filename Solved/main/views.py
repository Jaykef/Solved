from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def index_dark(request):
    return render(request, 'main/index_dark.html')
