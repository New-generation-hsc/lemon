from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project', views.project, name='project'),
    path('newtag', views.create_tag, name='tag'),
    path('newtask', views.create_task, name='task'),
    path('update/finish', views.update_task, name='update'),
    path('update/content', views.update_content, name='content'),
    path('project/<str:project>', views.retrive_project, name='rproject'),
    path('tag/<str:tag>', views.retrive_tag, name='rtag'),
]