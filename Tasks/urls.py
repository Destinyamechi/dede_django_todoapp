from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('taskform/', views.taskForm, name='taskform'),
    path('update/<str:pk>', views.updateTask, name='update_task'),
    path('delete/<str:pk>', views.deleteTask, name='delete_task'),

]