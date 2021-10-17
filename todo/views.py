from django.shortcuts import render, redirect
from  . models import Task
from . forms import Todoforms
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

# class TaskListView(generic.ListView):
#     model=Task
#     template_name = 'todo_home.html'
#     context_object_name = 'obj1'
#     def get_success_url(self):
#         return  reverse_lazy('')





def todo_home(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        obj=Task(name=name,age=age)
        obj.save()
    return render(request, "todo_home.html",{'obj1':obj1})


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = 'todo_update.html'
    context_object_name = 'task'
    fields = ('name','age')
    def get_success_url(self):
        return reverse_lazy('update',kwargs={'pk':self.object.id})

#
# def delete(request,task_id):
#     task = Task.objects.get(id=task_id)
#     if request.method=="POST":
#         task.delete()
#         return redirect('../../')
#     return render(request,'todo_delete.html',{'task':task})

#
# def update(request,id):
#     task = Task.objects.get(id=id)
#     form = Todoforms(request.POST or None, instance=task)
#     if form.is_valid():
#         form.save()
#         return redirect('../../')
#     return render(request,'todo_update.html',{'task':task,'form':form})

