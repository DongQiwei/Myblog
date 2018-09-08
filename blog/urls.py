from django.contrib import admin
from django.conf.urls import url, include
from blog import views

urlpatterns = [
    # ^ $ 以空字符开头 和结尾 斜杠不要忘记 /
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action/$', views.edit_action, name='edit_action'),
]
