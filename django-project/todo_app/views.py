from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import ToDoItem, ToDoList
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import ToDoItem, ToDoList

class LoginRequiredView(LoginRequiredMixin):
    login_url = 'login/'

@login_required
def entire_view_function(request):
    return render(request, 'index.html')

class ListListView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

    def get_queryset(self):
        return ToDoList.objects.filter(user=self.request.user)

class ItemListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list__user=self.request.user, todo_list_id=self.kwargs["list_id"])

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = get_object_or_404(ToDoList, id=self.kwargs["list_id"], user=self.request.user)
        return context

class ListCreate(LoginRequiredMixin, CreateView):
    model = ToDoList
    fields = ["title"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Add a new list"
        return context

class ItemCreate(LoginRequiredMixin, CreateView):
    model = ToDoItem
    fields = ["todo_list", "title", "description", "due_date", "completed"]

    def get_initial(self):
        initial_data = super().get_initial()
        todo_list = get_object_or_404(ToDoList, id=self.kwargs["list_id"], user=self.request.user)
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self):
        context = super().get_context_data()
        todo_list = get_object_or_404(ToDoList, id=self.kwargs["list_id"], user=self.request.user)
        context["todo_list"] = todo_list
        context["title"] = "Create a new item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = ToDoItem
    fields = ["todo_list", "title", "description", "due_date"]

    def get_context_data(self):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        context["title"] = "Edit item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])

class ListDelete(LoginRequiredMixin, DeleteView):
    model = ToDoList
    success_url = reverse_lazy("index")

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object.todo_list
        return context

@login_required
@require_POST
def mark_completed(request, list_id, item_id):
    todo_list = get_object_or_404(ToDoList, pk=list_id, user=request.user)
    todo_item = get_object_or_404(ToDoItem, pk=item_id, todo_list__user=request.user)

    todo_item.completed = True
    todo_item.save()

    return redirect(reverse("list", args=[list_id]))