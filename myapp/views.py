from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import registerdb, imagedb
# Create your views here.

def myfunction(request):
    return HttpResponse("<h1>HI<h1>")
def function2(request):
    return HttpResponse("BYE")

def firsthtmlpage(request):
    return render(request,"firstpage.html")
def registerpage(req):
    return render(req,"register.html")

def savedata(request):
     if request.method == "POST":
        na = request.POST.get('name')
        ag = request.POST.get('age')
        mo = request.POST.get('mob')
        obj = registerdb(name=na,Age=ag,Mobile=mo)
        obj.save()
        return redirect(registerpage)

def imgpage(req):
    return render(req,"imagepage.html")

def imagesave(request):
    if request.method == "POST":
        na = request.POST.get('name')
        img = request.FILES['image']
        obj = imagedb(name=na, Image=img)
        obj.save()
        return redirect(imgpage)

def img(request):
    return render(request,"image.html")
