from django.shortcuts import render,redirect
from .models import ToDoList
from django.contrib import messages

# Create your views here.
def index(request):
    lists = ToDoList.objects.order_by('-date')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        print(title, description)
        if date:
            ToDoList.objects.create(
                title = title, 
                description = description,
                date = date
            )
        else:
            ToDoList.objects.create(
                title = title,
                description = description,
            )
        messages.success(request, "New work has been created")
        return redirect('todolistIndex')
    
    return render(request, 'todolist/index.html', {'lists':lists,})

# from .form import ToDoForm
# def index(request):
#     lists = ToDoList.objects.order_by('-date')
#     if request.method == 'POST':
#         form = ToDoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todolistIndex')
#     else:
#         form = ToDoForm()   
#     return render(request, 'todolist/index.html' , {
#         'lists':lists,
#         'form':form
#     })

def deleteList(request, id):
    list_id = ToDoList.objects.get(id = id)
    messages.error(request, f"The work with title {list_id.title} has been deleted!")
    list_id.delete()
    return redirect('todolistIndex')
