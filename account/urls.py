from django.conf.urls import url

from . import views

urlpatterns = [
    url('login', views.login, name='login'),
    url('registe', views.registe, name='registe'),
]