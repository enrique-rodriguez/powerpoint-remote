import keyboard
import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


logging.basicConfig(level=logging.INFO)


def home(request):
    return render(request, 'app/index.html')


@csrf_exempt
def send_key(request):
    key = request.GET.get('key')
    if request.method.lower() == "post":
        logging.info(f"Pressing key '{key}'")
        keyboard.press_and_release(key)
    return HttpResponse(status=200)