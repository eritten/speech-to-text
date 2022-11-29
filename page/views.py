from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

from rest_framework.response import Response
from rest_framework.decorators import api_view
import pyttsx3 as pt

def say(text):
    e = pt.init()
    e.setProperty("rate", 140)
    e.say(text)
    e.runAndWait()

@api_view(["GET"])
def listen(request):
    try:
        name = request.GET.get("name")
        description = request.GET.get("descript")
        price = request.GET.get("price")
        manu = request.GET.get("manu")
    except Exception as e:
        return Response({"status": str(e)})
    text = "Please the slected item is " + name + ". " + description + " the price is " + price + " manufactured by " + manu
    say(text)
    return Response({"status": "ok"})
