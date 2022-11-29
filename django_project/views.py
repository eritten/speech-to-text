from rest_framework.response import Response
from rest_framework.decorators import api_view
import pyttsx3 as pt

def say(text):
    e = pt.init()
    e.setProperty("rate", 140)
    e.say(text)
    e.runAndWait()
@api_view(["GET"])
def speak(request):

    return Response({"status": "ok"})
