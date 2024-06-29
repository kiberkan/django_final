from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout,authenticate
from .forms import RecipeForm
from .models import Recipe,RecipeCategory
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from datetime import datetime
from .models import RecipeCategoryRelationship


def home(request):
    categories = RecipeCategory.objects.all()
    recipe_relationships = RecipeCategoryRelationship.objects.all().order_by('-id')[:5]
    return render(request, 'home.html', {'categories': categories, 'recipe_relationships': recipe_relationships})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})





@login_required(login_url='/accounts/login/')  
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.image = request.FILES['image']
            
            current_time = datetime.now().strftime("%Y%m%d%H%M%S%f")
            file_extension = recipe.image.name.split('.')[-1]
            file_name = f"{current_time}.{file_extension}"
            recipe.image.name = file_name
            recipe.save()

            category_id = request.POST.get('category')
            category = RecipeCategory.objects.get(pk=category_id)
            RecipeCategoryRelationship.objects.create(recipe=recipe, category=category)
            
            return redirect('home')
    else: 
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        recipe_category_relationships = RecipeCategoryRelationship.objects.filter(recipe=recipe)
        if recipe_category_relationships.exists():
            category = recipe_category_relationships.first().category
        else:
            category = None
        form = RecipeForm(instance=recipe, initial={'category': category})

    return render(request, 'recipe_form.html', {'form': form, 'recipe': recipe})




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Неправильный пароль или имя пользователя.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан "{username}"')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
