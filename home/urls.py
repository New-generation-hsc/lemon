from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    url('project', views.project, name='project'),
    url('newtag', views.create_tag, name='tag'),
    url('newtask', views.create_task, name='task'),
    url('update/finish', views.update_task, name='update'),
    url('update/content', views.update_content, name='content'),
    url('project/<str:project>', views.retrive_project, name='rproject'),
    url('tag/<str:tag>', views.retrive_tag, name='rtag'),
]