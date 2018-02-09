from django.shortcuts import render, redirect
from .models import TgUser

# Create your views here.

def index(request):
    return render(request, "index.html", {})

def register(request):
    user, created = TgUser.get_or_create(tg_id=request.POST.get('id', ''))
    user.tg_first_name = request.POST.get('first_name', '')
    user.tg_last_name = request.POST.get('last_name', '')
    user.tg_username = request.POST.get('username', '')
    user.tg_photo_url = request.POST.get('photo_url', '')
    user.tg_auth_date = request.POST.get('auth_date', '')
    user.tg_hash = request.POST.get('hash', '')
    if user.check_hash():
        user.save()
    else:
        return render(request, 'error.html', {
            'msg': 'Bad hash!'
        })
    return redirect('/')
