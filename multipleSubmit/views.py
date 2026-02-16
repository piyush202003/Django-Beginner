from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if 'subscribe' in request.POST and email != '':
            MultipleSubmit.objects.create(
                email = email,
                subscribe = 'sub'
            )
            messages.success(request, f'This {email} has been saved as Subscribe')
        elif 'unsubscribe' in request.POST and email != '':
            MultipleSubmit.objects.create(
                email = email,
                subscribe = 'unsub'
            )
            messages.success(request, f'This {email} has been saved unsubscribe')
        else:
            messages.warning(request, 'Something went wrong')
        
        return redirect('multipleSubmitIndex')
    return render(request, 'multipleSubmit/index.html')