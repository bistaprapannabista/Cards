from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Card
import random
# Create your views here.

def index(request):
    if not request.session.has_key('name'):
        return redirect('/')
    cards = list(Card.objects.all())
    random.shuffle(cards)
    context = {
        'cards':cards
    }
    return render(request,'index.html',context)

def initial(request):
    if request.method=="POST":
        request.session['name'] = request.POST['name']
        request.session['amount'] = request.POST['amount']
        return redirect('home')
    return render(request,'initial.html')

def _computerChoice():
    return random.choice(list(Card.objects.all()))

def play(request,id):

    if not request.session.has_key('name'):
        return redirect('/')

    human_choice = Card.objects.get(id=id)
    computer_choice = _computerChoice()
    name = request.session['name']
    while(human_choice==computer_choice):
        computer_choice = _computerChoice()

    if(human_choice.value > computer_choice.value):
        result = "won"
        amount = 2*int(request.session['amount'])
    elif(human_choice.value < computer_choice.value):
        result = "lose"
        amount = 0
    else:
        result= "tie"
        amount = request.session['amount']

    del request.session['name']
    del request.session['amount']

    context = {
        'result':result,
        'human_choice':human_choice,
        'computer_choice':computer_choice,
        'name':name,
        'amount':amount
    }

    return render(request,'final.html',context)
