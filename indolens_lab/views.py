from django.http import HttpResponse


def checkLogin(request):  # new
    return HttpResponse('<h1>WELCOME INDOLENS LAB</h1>')
