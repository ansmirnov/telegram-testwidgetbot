import os
import requests

from django.shortcuts import render, redirect

from .models import TgUser
from .utils import HashCheck


# Create your views here.

def index(request):
    try:
        user_id = int(request.session['user_id'])
        user = TgUser.objects.get(id=user_id)
        return render(request, "welcome.html", {'user': user})
    except:
        return render(request, "index.html", {})

def register(request):
    secret = os.getenv('BOT_TOKEN').encode('utf-8')
    if not HashCheck(request.GET, secret).check_hash():
        return render(request, 'error.html', {
            'msg': 'Bad hash!'
        })
    user = TgUser.make_from_dict(request.GET)
    user.save()
    request.session['user_id'] = user.id
    return redirect('/')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def send(request):
    try:
        user_id = int(request.session['user_id'])
        user = TgUser.objects.get(user_id)
    except:
        return render(request, 'error.html', {
            'msg': 'You are not logged in!'
        })
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = user.tg_id
    text = "Hello!"
    url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(bot_token, chat_id, text)
    requests.get(url)
