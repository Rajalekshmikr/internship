from django.shortcuts import render,redirect
from . models import Task
# from . forms import Taskform
# from django.http import HttpResponse


# Create your views here.
def add(request):
  if request.method=='POST':
      name=request.POST.get('task','')
      priority=request.POST.get('priority','')
      finished=request.POST.get('finished')
      task=Task(name=name,priority=priority,finished=finished)
      task.save()

  return render(request,"home.html")
  # return HttpResponse("hello welcome to todo")

