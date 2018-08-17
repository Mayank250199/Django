from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.article),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail)
]
