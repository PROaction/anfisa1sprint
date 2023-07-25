from django.shortcuts import render


def index(request):
    template = 'homepage/index_1.html'
    return render(request, template)
