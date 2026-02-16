from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import Plans
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib import messages

# Create your views here.
@login_required(login_url='RMPLogin')
@never_cache
def index(request):
    recipes = Plans.objects.filter(user=request.user)
    if request.method == 'POST':
        day = request.POST.get('day')
        name = request.POST.get('name')
        description = request.POST.get('description')
        Plans.objects.create(
            user = request.user,
            day = day,
            name = name,
            description = description
        )
        messages.success(request, 'New recipe has been added')
        return redirect('RMPIndex')
    search = request.GET.get('search')
    if search:
        # search = search.lower()
        recipes = recipes.filter(day__icontains = search)
        print(recipes)
    return render(request, 'RecipeMealPlanner/index.html', {'recipes':recipes})

@login_required(login_url='RMPLogin')
def editRecipe(request, pk):
    data_obj = Plans.objects.get(pk=pk)
    if request.method == 'POST':
        day = request.POST.get('day')
        name = request.POST.get('name')
        description = request.POST.get('description')
        data_obj.day = day
        data_obj.name = name
        data_obj.description = description
        data_obj.save()
        messages.success(request, f'Recipe with name {name} at {day} has been updated!!')
        return redirect('RMPIndex')
    return render(request, 'RecipeMealPlanner/editRecipe.html',{'data':data_obj})

@login_required(login_url='RMPLogin')
def deleteRecipe(request, pk):
    data_obj = Plans.objects.get(pk=pk)
    messages.warning(request, f'Your plan of {data_obj.day} Day-Time and Name {data_obj.name} has been deleted!!')
    data_obj.delete()
    return redirect('RMPIndex')

def loginPage(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_data = User.objects.filter(username = username)
            if not user_data:
                redirect('RMPLogin')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                messages.success(request, f"{username} has been succefully logged in!!")
                return redirect('RMPIndex')
            messages.warning(request, 'You are useing the wrong password!!')
            return redirect('RMPLogin')
        except Exception as e:
            messages.warning(request, 'Something went wrong!!')
            return redirect('RMPLogin')
    return render(request, 'RecipeMealPlanner/login.html')

def register(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj:
                messages.warning(request, 'This username alread exists! Try with different username.')
                redirect('RMPRegister')
            user_obj = User.objects.create(username = username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, f"New account with username {username} has been created")
            return redirect('RMPLogin')
        except Exception as e:
            messages.warning(request, 'Something went wrong!!')
            return redirect('RMPRegister')
    return render(request, 'RecipeMealPlanner/register.html')

def custom_logout(request):
    logout(request)
    messages.info(request, "Your account has been succefully Logged Out")
    return redirect('RMPLogin')
    
@login_required(login_url='RMPLogin')
def pdf(request):
    recipes = Plans.objects.filter(user = request.user)
    search = request.GET.get('search')
    if search:
        # search = search.lower()
        recipes = recipes.filter(day__icontains = search)
    return render(request, 'RecipeMealPlanner/pdfRecipe.html', {'recipes':recipes})