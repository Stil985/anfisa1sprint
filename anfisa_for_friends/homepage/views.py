from django.shortcuts import render


def index(request):
    print('Test')
    template = 'homepage/index.html'
    return render(request, template)
