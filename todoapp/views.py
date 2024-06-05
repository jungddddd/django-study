from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView

from todoapp.decorators import todo_ownership_required
from todoapp.forms import TodoCreationForm
from todoapp.models import Todo

# Create your views here.
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoCreationForm
    template_name = 'todoapp/create.html'

    def form_valid(self, form):
        temp_todo = form.save(commit=False)
        temp_todo.todo = Todo.objects.get(
            pk=self.request.POST['todo_pk'])
        temp_todo.writer = self.request.user
        temp_todo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todoapp:detail', kwargs={'pk': self.object.pk})

    @method_decorator(todo_ownership_required, 'get')
    @method_decorator(todo_ownership_required, 'post')
    class TodoUpdateView(UpdateView):
        model = Todo
        context_object_name = 'target_todo'
        form_class = TodoCreationForm
        template_name = 'todoapp/update.html'

        def get_success_url(self):
            return reverse('todoapp:detail', kwargs={'pk': self.object.pk})

        # 완료되지 않는 todo 필터링하는 템플릿
        def todo_list(request):
            todos = Todo.objects.filter(completed=False)
            return render(request, 'todo/todo_list.html', {'todos': todos})

        def todo_done(request, pk):
            todo = Todo.objects.get(id=pk)
            todo.completed = True
            todo.save()
            return redirect('todo_list')

        def todo_done_list(request):
            dones = Todo.objects.filter(completed=True)
            return render(request, 'todo/todo_done_list.html',{'dones':dones})









