from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetaisToDo.as_view(), name='update'),
    path('', ListTodo.as_view(), name='desplay'),
    path('create', CreateTodo.as_view(), name='create'),
    path('delete/<int:pk>', DeleteToDo.as_view(), name='delete')
]