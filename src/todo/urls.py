from django.urls import path

from .views import (TodoCreateView, TodoDeleteView, TodoDetailView,
                    TodoListView, TodoUpdateView)

app_name = "todo"
urlpatterns = [
    path('', TodoListView.as_view(),name='todo-list'),
    path('update/<str:pk>/', TodoUpdateView.as_view(),name='todo-update'),
    path('create', TodoCreateView.as_view(),name='todo-create'),
    path('detail/<str:pk>/', TodoDetailView.as_view(),name='todo-detail'),
    path('delete/<str:pk>/', TodoDeleteView.as_view(),name='todo-delete'),
]