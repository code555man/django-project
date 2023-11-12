from django.shortcuts import render, redirect
from myapp.models import Person
from django.contrib import messages
# Create your views here.

def home(request):
    persons = Person.objects.all()
    return render(request,'myapp/home.html',{'persons': persons})
def about(request):
    return render(request,'myapp/about.html')
def form(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        
        person = Person.objects.create(name=name,age=age)
        person.save()
        messages.success(request,'Save Data Success')
        return redirect('form')
    else:
        return render(request,'myapp/form.html')
    
def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST['name']
        person.age = request.POST['age']
        person.save()
        messages.success(request,'Update Data Success')
        return redirect('form')
        
    else:
        person = Person.objects.get(id=person_id)
        return render(request, 'myapp/edit.html',{'person': person})
    
def delete(request,person_id):
    person = Person.objects.get(id=person_id)
    person.delete()
    messages.success(request,'Delete Data Success')
    return redirect('home')