from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    # Код для обработки запроса и формирования контекста
    return render(request, 'home_page/index.html')
