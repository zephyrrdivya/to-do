from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.views import View

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from datetime import datetime
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm


class TaskList(LoginRequiredMixin, ListView):
    model = Task


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task


@login_required
def home(request):
    instances = Task.objects.filter(user=request.user).order_by(
        'isCompleted', '-last_updated')
    context = {
        'title': 'Home',
        'tasks': instances,
        # 'days':
    }
    return render(request, 'tasks/task_list.html', context)


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'tasks/task_form.html'
    form_class = TaskForm

    def get(self, request, *args, **kwargs):
        taskform = self.form_class

        context = {
            'form': taskform,
            'title': 'New Task',
            'value': 'Add New Task',
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, self.template_name, context)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ('title', 'content', 'deadline_date')
    template_name = 'tasks/task_form.html'

    # form_class = TaskForm

    def get(self, request, *args, **kwargs):
        self.object = Task.objects.get(id=self.kwargs['pk'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = {
            'form': form,
            'title': 'Update Task',
            'value': 'Update Task',
        }
        return render(request, self.template_name, context)

    def form_valid(self, form):
        task = form.save(commit=False)
        task.user = self.request.user
        task.last_updated = datetime.now()
        task.save()
        return redirect('home')
        # form = self.form_class(request.TASK)
        # if form.is_valid():
        #     form.save(request)
        #     return HttpResponseRedirect(reverse('home'))
        # else:
        #     return render(request, self.template_name, context)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def done_task(request, pk):
    try:
        task = get_object_or_404(Task, pk=pk, user=request.user)
        task.isCompleted = True
        task.save()
        return HttpResponseRedirect(reverse('home'))
    except:
        pass


# @login_required
# def update_task(request, id):
#     task = get_object_or_404(Task, id=id, user=request.user)
#     print(task.id)
#     if request.user == task.user:
#         form = TaskForm(request.TASK or None, instance=task)

#         if form.is_valid():
#             instance = form.save(request, commit=False)
#             instance.save()
#             return redirect("home")

#         context = {
#             'instance': task,
#             'form': form,
#             'title': "Update task Details",
#             'value': 'Update Details'
#         }
#         return render(request, "tasks/task_form.html", context)
#     return HttpResponse('Task not Found')


# @login_required
# def delete_task(request, id):
#     try:
#         _ = get_object_or_404(Task, id=id, user=request.user).delete()
#         return HttpResponseRedirect(reverse('home'))
#     except:
#         pass
