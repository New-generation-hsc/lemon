from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Category, Tag, Task
from .forms import ValidateFrom, TaskForm

# Create your views here.
@login_required(login_url='/account/login')
def index(request):
    projects = Category.objects.filter(owner=request.user)
    tags = Tag.objects.filter(owner=request.user)
    tasks = Task.objects.filter(owner=request.user, finished=False)
    finished_tasks = Task.objects.filter(owner=request.user, finished=True)
    context = {
        'projects' : projects,
        'tags' : tags,
        'tasks' : tasks,
        'finished_tasks' : finished_tasks
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
            return JsonResponse({'msg' : "创建清单" + name + "成功"})
        return JsonResponse({'msg' : "创建清单" + name + "失败"})
    return redirect('/')

@login_required(login_url='/account/loign')
def create_tag(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        color = request.POST.get('color', '')
        form = ValidateFrom(request.POST, user=request.user, model=Tag)
        if form.is_valid():
            Tag.objects.create_tag(request, name, color)
            return JsonResponse({'msg' : "创建标签" + name + "成功"})
        return JsonResponse({'msg' : "创建标签" + name + "失败"})
    return redirect('/')


@login_required(login_url='/account/login')
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            task = Task(content=data['content'], remind_time=data['remind_time'])
            task.owner = request.user
            pk = int(request.POST.get('radio', '0'))
            category = Category.objects.get(pk=pk)
            task.category = category
            task.save()
            for key in request.POST:
                if key.startswith('check'):
                    pk = int(request.POST[key])
                    tag = Tag.objects.get(pk=pk)
                    task.tags.add(tag)
            return JsonResponse({'msg': '创建任务成功'})
        return JsonResponse({'msg' : '创建任务失败'})
    return redirect('/')


@login_required(login_url='/account/login')
def update_task(request):
    if request.method == "POST":
        pk = request.POST.get('pk', '')
        if pk:
            task = Task.objects.get(pk=pk)
            task.finished = not task.finished
            task.save()
            print("update succ")
            return JsonResponse({"msg" : "更新任务成功"})
        return JsonResponse({'msg' : "更新任务失败"})
    return redirect('/')