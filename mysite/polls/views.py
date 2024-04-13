# polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("¡Hola, mundo! Estás en el índice de encuestas.")