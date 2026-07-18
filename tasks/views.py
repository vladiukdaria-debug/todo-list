from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

from tasks.forms import TagForm, TaskForm
from tasks.models import Tag, Task


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "task_list"

    def get_queryset(self):
        return (
            Task.objects
            .prefetch_related("tags")
            .order_by("is_done", "-created_at")
        )


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_form.html"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:task-list")


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save(update_fields=["is_done"])

        return redirect("tasks:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tag_list"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "tasks/tag_form.html"


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tag-list")
