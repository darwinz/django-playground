from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world.  This is Django Brown from Phineas and Ferb.")
