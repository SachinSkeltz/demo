from django.shortcuts import render,redirect

def about(request):
    return render(request,"about.html")
#
#
def gallery(request):
    return render(request,"gallery.html")
#
#
def contact(request):
    return render(request,"contact.html")
#
#
def products(request):
    return render(request,"products.html")
#
def home(request):
    return redirect('/')