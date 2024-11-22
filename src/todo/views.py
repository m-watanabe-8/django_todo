from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,UpdateView,CreateView,DetailView,DeleteView

from .models import TodoModel
from .forms import  TodoModelForm

# 一覧
class TodoListView(ListView):
    template_name = 'todo/todo-list.html'
    model = TodoModel

# 更新
class TodoUpdateView(UpdateView):
    template_name = 'todo/todo-form.html'
    model = TodoModel
    form_class = TodoModelForm
    success_url = reverse_lazy("todo:todo-list")

# 新規作成
class TodoCreateView(CreateView):
    template_name = 'todo/todo-form.html'
    form_class = TodoModelForm
    success_url = reverse_lazy("todo:todo-list")
    
# 詳細
class TodoDetailView(DetailView):
    template_name = 'todo/todo-detail.html'
    model = TodoModel

# 削除機能
class TodoDeleteView(DeleteView):
    template_name = 'todo/todo-form.html'
    model = TodoModel
    success_url = reverse_lazy("todo:todo-list")

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)