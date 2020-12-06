from django.shortcuts import render, redirect


from fbchat import Client
from fbchat.models import *


def chat(request):
    messeges = client.fetchThreadMessages(thread_id=uid, limit=50)

    if request.POST.get('sendtext'): 
        txt = request.POST.get('txt')
        client.send(Message(text = txt), thread_id=uid, thread_type=ThreadType.USER)

    return render(request, 'chat.html', {
        'messeges':messeges,
        })



def getData(request):
    users = client.fetchAllUsers()

    if request.POST.get('open'): 
        global uid
        uid = request.POST.get('open')
        return redirect('chat')

    return render(request, 'users.html', {
        'users':users,
        })




def loginUser(request, number, password):
    global client
    client = Client(number, password)
    return

def login(request):

    if request.POST.get('login'): 
        tlfNumber = request.POST.get('tlfNumber')
        password = request.POST.get('Password')

        loginUser(request, tlfNumber, password)
        if client.isLoggedIn():
            return redirect('data')
    

    return render(request, 'index.html', {})
