from django.shortcuts import render, render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'attempt' in request.session:
        request.session['attempt'] = 0
        request.session['rand_word'] = 'Try it!'
    return render(request, 'index.html')

def random_word(request):  
    rand_word = get_random_string(length=14)
    request.session['rand_word'] = rand_word
    request.session['attempt'] +=1    
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
