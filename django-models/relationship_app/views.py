# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
