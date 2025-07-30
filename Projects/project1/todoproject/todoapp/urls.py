from django.urls import path
from todoapp.views import task_list, task_create, task_update, task_delete, task_toggle

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:task_id>/', task_update, name='task_update'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
    path('toggle/<int:task_id>/', task_toggle, name='task_toggle'),
]
