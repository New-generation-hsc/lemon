from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Tag
from .forms import ValidateFrom

# Create your views here.
@login_required(login_url='/account/login')
def index(request):
    projects = Category.objects.filter(owner=request.user)
    tags = Tag.objects.filter(owner=request.user)
    context = {
        'projects' : projects,
        'tags' : tags
    }
    return render(request, 'home.html', context=context)

@login_required(login_url='/account/loign')
def project(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        form = ValidateFrom(request.POST, user=request.user, model=Category)
        if form.is_valid():
            Category.objects.create_category(request, name, color)
    return redirect('/')

@login_required(login_url='/account/loign')
def create_tag(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        form = ValidateFrom(request.POST, user=request.user, model=Tag)
        if form.is_valid():
            Tag.objects.create_tag(request, name, color)
            print("create tag succ", name, color)
    return redirect('/')


@login_required(login_url='/account/login')
def create_task(request):
    if request.method == "POST":
        print(request.POST)
    return redirect('/')