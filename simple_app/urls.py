from django.conf.urls import url

from simple_app import views

urlpatterns = [url(r'^$', views.index, name='index'),]
