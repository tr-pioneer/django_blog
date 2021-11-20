from django.core.exceptions import RequestAborted
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView, ListView, DetailView,CreateView, UpdateView, DeleteView
from .models import User    
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = 'blog/home.html'

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    paginate_by = 3

class UserDetailView(DetailView):
    model = User


def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect('home')
    
    context = {
        'form_user': form
    }
    return render(request, 'blog/register.html', context)

def user_logout(request):
    messages.success(request, "You are logged out!")
    logout(request)
    return redirect('home')

def user_login(request):
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull!")
            login(request, user)
            return redirect('home')
    return render(request, 'blog/user_login.html', {'form':form})






    