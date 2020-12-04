from django.urls import path
from morningapp import api
urlpatterns = [
    path('morn-register/',api.morn_register),
    path('morn-login/',api.morn_login),
    # 文章操作
    path('add-article/',api.add_article),
    path('get-articlelist/',api.get_articlelist),
    path('get-article/',api.get_article),
    path('del-article/',api.del_article),
    path('get-tag/',api.get_tag)
]