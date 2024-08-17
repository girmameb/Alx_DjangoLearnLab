# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # Redirect to a home or any other page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to a home or any other page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'profiles/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'profiles/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'profiles/member_view.html')