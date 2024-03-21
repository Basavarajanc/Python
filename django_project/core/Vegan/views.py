from django.shortcuts import redirect, render

from Vegan.models import Recipe

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

