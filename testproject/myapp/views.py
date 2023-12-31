from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout 


def hello(request, _id):
    return HttpResponse('hello' + str(_id))

def article(request, year, slug):
    return HttpResponse('Article' + str(year) + str(slug))

def index(request):
    return render(request, 'index.html')

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book:index')
    else:    
        form = AuthenticationForm()
    return render(request, 'account/login.html',{
        'form': form,
    })
    
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('myapp:index')
    
    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book:index')
    else:    
        form = UserCreationForm()
    return render(request, 'account/signup.html',{
        'form': form,
    })