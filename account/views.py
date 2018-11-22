from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import AccountForm

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(request, username=username, password=password)
        if not user and username and password:
            auth.login(request, user)
            return redirect('/account/login')
    return render(request, 'login.html')

def registe(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            auth.models.User.objects.create_user(username=data['username'],
                                                 email=data['email'],
                                                 password=data['password'])
            user = auth.authenticate(request, username=data['username'], password=data['password'])
            auth.login(request, user)
            print("create user succ", data['username'])
            return redirect('/account/login')
    return render(request, 'signup.html')