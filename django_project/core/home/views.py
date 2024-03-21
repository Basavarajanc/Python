from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    people_data = [{'name' : 'Basa', 'age' : 17}, {'name' : 'Basa1', 'age' : 55}, {'name' : 'Basa2', 'age' : 26}, {'name' : 'Basa3', 'age' : 30}]

    
    return render(request,"index.html", context = {"people_data" : people_data} )

def next_page(request):
    return HttpResponse("<h2><strong>basav here</strong></h2>")

def about(request):
    return render(request,"about.html", context = {"title" : "ABOUT"} )

def contact(request):
    return render(request,"contact.html", context = {"title" : "CONTACT"} )

def services(request):
    return render(request,"services.html", context = {"title" : "SERVICES"} )
