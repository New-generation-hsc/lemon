from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Tag

# Create your views here.
@login_required(login_url='/account/login')
def index(request):
    return render(request, 'home.html')

@login_required(login_url='/account/loign')
def project(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        if name and color:
            Category.objects.create_category(request, name, color)
    return redirect('/')

@login_required(login_url='/account/loign')
def create_tag(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        if name and color:
            Tag.objects.create_tag(request, name, color)
            print("create tag succ", name, color)
    return redirect('/')        