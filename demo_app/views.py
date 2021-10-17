from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import featured_items
from . form import ModelForm
from django.views import generic


def demo(request):
    obj=featured_items.objects.all()
    return render(request,"index.html",{'results':obj})


def detail(request,featured_items_id):
    obj1 = featured_items.objects.get(id=featured_items_id)
    return render(request,"detail.html",{'items':obj1})

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc= request.POST.get('desc')
        img = request.FILES['img']
        s=featured_items(name=name,desc=desc,img=img)
        s.save()
    return render(request,"add_products.html")

def update(request,id):
    obj = featured_items.objects.get(id=id)
    form=ModelForm(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html',{'form':form,'obj':obj})

def delete(request,id):
    if request.method=='POST':
        obj=featured_items.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')