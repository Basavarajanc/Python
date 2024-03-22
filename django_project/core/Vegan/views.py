from django.shortcuts import redirect, render

from Vegan.models import Recipe

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

@login_required(login_url="/login_page")
def Recepies(request):
    if request.POST :
        data = request.POST
        recipename = data.get('recipe_name')
        recipedesc = data.get('recipe_desc')
        recipeimage = request.FILES['recipe_image']
        
        Recipe.objects.create(recipe_name = recipename,
                              recipe_desc = recipedesc,
                              recipe_image = recipeimage )

    
    querySet = Recipe.objects.all()
        
    context = {
            "title" : "Add Recipes",
            "recipes": querySet}
        
    return render(request, "recepies.html", context)

def Delete_recipe(request, id):
    querySet = Recipe.objects.get(id = id)
    querySet.delete()
    
    return redirect('/Recepies')

def Update_recepie(request, id):
    querySet = Recipe.objects.get(id = id)
    context = {
            "title" : "Update Recipes",
            "recipes": querySet}
    
    if request.POST :
        data = request.POST
        recipename = data.get('recipe_name')
        recipedesc = data.get('recipe_desc')
        recipeimage = request.FILES['recipe_image']
        
        querySet.recipe_name = recipename
        querySet.recipe_desc = recipedesc
        querySet.recipe_image = recipeimage
        
        querySet.save()
        
        return redirect('/Recepies')
    return render(request, "update_recepies.html", context)

def login_page(request):
     context = {
            "title" : "Login"
            }
     
     if request.POST:
         data = request.POST
         username = data.get('username')
         password = data.get('password')
         
         if not User.objects.filter(username = username).exists():
           messages.info(request, "invalid user")
           return redirect('/login_page', context)
     
         user = authenticate(username = username , password = password)
     
         if user is None:
          messages.info(request, "invalid password")
          return redirect('/login_page', context)
    
         else:
          login(request, user)
          return redirect('/Recepies')
    
     return render(request, "login.html", context)
 
def register(request):
     context = {
            "title" : "Register"
            }
     
     if request.POST:
         data = request.POST
         first_name = data.get('first_name')
         last_name = data.get('first_name')
         username = data.get('username')
         password = data.get('password')
         
         userExists = User.objects.filter(username =  username)
         
         if userExists.exists():
            messages.info(request, "User name already taken")
            return redirect('/register')
         
         user = User.objects.create(
             first_name = first_name,
             last_name = last_name,
             username = username
         )
       
         user.set_password(password)
         user.save()
         
         messages.info(request, "User created successfully")
         return redirect('/register')
     
     return render(request, 'register.html', context)

