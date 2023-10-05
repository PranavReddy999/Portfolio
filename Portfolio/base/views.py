from django.shortcuts import render
from base.models import Contact
# Create your views here.
def base(request):
    return render(request,'base.html')
def contact(request):
    if request.method=="POST":
        name=request.POST['exampleFormControlInput1']
        email=request.POST['exampleFormControlInput2']
        comment=request.POST['exampleFormControlTextarea1']
        print(name,email,comment) 
        ins=Contact(name=name,email=email,comment=comment)
        ins.save()
        print("data stored")
    return render(request,'contact.html')
def home(request):
    return render(request,'home.html')
def skills(request):
    return render(request,'skills.html')
def projects(request):
    return render(request,'projects.html')
