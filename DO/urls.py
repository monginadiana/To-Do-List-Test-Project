from django.urls import path
# from django.contrib import admin
from .import views
# from . import views as app_views

urlpatterns = [
    path('',views.index ,name = 'index'),
    path('create/',views.create ,name = 'create'),
    path('single/<int:todo_id>',views.singleToDo ,name = 'single'),
    path('update/<int:todo_id>',views.update_todo ,name = 'update'),
    path('<int:todo_id>/delete', views.delete_todo, name='delete_todo'),

]