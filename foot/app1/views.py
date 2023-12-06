from django.shortcuts import render
from .models import dis
from .forms import bookingform

# Create your views here.
def index(request):
    return render(request,'index.html')
def display(request):
    dict_dis={'name':dis.objects.all()}
    return render(request,'display.html',dict_dis)
def about(request):
    return render(request,'about.html')
def games(request):
    return render(request,'games.html')
def books(request):
    if request.method=="POST":
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'index.html')
    form=bookingform()
    dict_book={'form':form}
    return render (request,'book.html',dict_book)