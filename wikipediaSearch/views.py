from django.shortcuts import render
from django.contrib import messages
import wikipedia
# Create your views here.
def home(request):
    if request.method == 'POST':
        search = request.POST['search']
        try:
            response = wikipedia.summary(search, sentences=5)
            messages.success(request, "Here is your result")
        except:
            messages.error(request, "Search did not found")
            return render(request, 'wikipediaSearch/index.html')
        return render(request, 'wikipediaSearch/index.html', {'response':response})
    return render(request, 'wikipediaSearch/index.html')