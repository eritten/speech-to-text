from django.shortcuts import render
from voice_bot.decorators import add_bot

# Create your views here.
@add_bot(bot_name="love")
def home(request, **kwargs):
    return render(request, 'home.html', {"commands": kwargs["commands"], "bot_name": kwargs["bot_name"], "speech_full": True})

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
