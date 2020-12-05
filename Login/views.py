from django.shortcuts import render, redirect


from fbchat import Client
from fbchat.models import *
import time

def loginUser(number, password):

    client = Client(number, password)
    return client


def chat(request, number, password):

    client = loginUser(number, password)
    chats = client.fetchAllUsers()

    return render(request, 'chat.html', {'chats':chats})




def login(request):

    if request.POST.get('login'): 
        tlfNumber = request.POST.get('tlfNumber')
        password = request.POST.get('Password')

        return chat(request, tlfNumber, password)

    return render(request, 'index.html', {})
