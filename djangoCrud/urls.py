from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='Home'),
    path('singup/', views.SingUp, name='SingUp'),
    path('tasks/completed', views.Tasks_Completed,
         name='Tasks_Completed'),  # muestra tareas completas
    path('task/', views.GetTask, name='Task'),
    path('logout/', views.SingOut, name='SingOut'),
    path('singin/', views.SingIn, name='SingIn'),
    path('task/create/', views.CreateTask, name='CreateTask'),
    path('task/<int:task_id>', views.TaskDetail, name='TaskDetail'),
    path('task/<int:task_id>/complete', views.CompleteTask,
         name='CompleteTask'),  # marcar una tarea
    path('task/<int:task_id>/delete', views.DeleteTask, name='DeleteTask'),
]
