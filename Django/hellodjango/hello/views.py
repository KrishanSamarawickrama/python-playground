from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(reqest):
    return render(reqest, 'hello/index.html')

# def great(reqest, name):
#     return HttpResponse(f"Hello, {name.capitalize()} !!")

def great(reqest, name):
    return render(reqest, "hello/great.html",{
        "name": name.capitalize()
    })