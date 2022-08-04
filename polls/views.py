from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello there, you're at polls INDEX.")
