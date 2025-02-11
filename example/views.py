from django.shortcuts import render,redirect
from .models import *
def home(request):
    return render(request, 'home.html')
def recepies(request):
    if request.method=="POST" :
        recepie.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            image=request.FILES['image']
           

        )
      
    return render(request,'recepies.html',{'recepies':recepie.objects.all()})
def delete_recepie(request,id):

    recepie.objects.filter(id=id).delete()
    return redirect('recepies')
def update_recepie(request,id):
    recepie.objects.filter(id=id)