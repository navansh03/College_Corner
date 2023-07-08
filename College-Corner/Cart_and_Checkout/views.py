from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# @login_required(login_url=' /login/')
def cartcalling(request):
    return cartcalling2(request)


def cartcalling2(request):
    return render(request,'Cart.html')


