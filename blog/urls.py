from django.urls import path
from . import views

"""
视图函数
"""
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.detail, name='detail' )

]