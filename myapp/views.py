from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def home(request):   
    return render(request, 'myapp/home.html')



def simple_view(request):
    return HttpResponse("Hello, world!")

from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection

from django.http import JsonResponse

def my_view(request):

    table1_data = [
        {"id": 1, "name": "Item A", "value": 10},
        {"id": 2, "name": "Item B", "value": 20}
    ]

    table2_data = [
        {"id": 1, "description": "Description A", "quantity": 5},
        {"id": 2, "description": "Description B", "quantity": 15}
    ]

    data = {
        "table1": table1_data,
        "table2": table2_data
    }

    return JsonResponse(data)

def my_view1(request):
    
    table1_data = [
        {"id": 3, "name": "Item A", "value": 10},
        {"id": 4, "name": "Item B", "value": 20}
    ]

    # Return the data as a JSON response
    return JsonResponse(table1_data)



