from django.http import HttpResponse


def index(request):  # new
    return HttpResponse('<h1>WELCOME TO INDOLENS PUBLIC WEBSITE</h1>')
