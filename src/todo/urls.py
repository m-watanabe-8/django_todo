from django.urls import path, re_path, include
from .views import TodoListView,TodoUpdateView,TodoCreateView,TodoDetailView,TodoDeleteView

app_name = "todo"
urlpatterns = [
    path('', TodoListView.as_view(),name='todo-list'),
    re_path(r'update/(?P<pk>[\w-]+)/$', TodoUpdateView.as_view(),name='todo-update'),
    path('create', TodoCreateView.as_view(),name='todo-create'),
    re_path(r'detail/(?P<pk>[\w-]+)/$', TodoDetailView.as_view(),name='todo-detail'),
    re_path(r'delete/(?P<pk>[\w-]+)/$', TodoDeleteView.as_view(),name='todo-delete'),
]