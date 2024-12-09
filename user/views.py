from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import logout, update_session_auth_hash

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from .forms import RegisterForm, ChangeUserData


def signup(request):
    if request.method == 'POST':
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            messages.success(request, 'Account created successfully')
            registerForm = RegisterForm()
        else:
            messages.error(request, 'There was an error creating your account')
    else:
        registerForm = RegisterForm()

    return render(request, 'signup.html', {'form': registerForm,})

class UserLoginView(LoginView):
    template_name = 'signin.html'

    def get_success_url(self) -> str:
        return reverse_lazy('profile')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Please provide correct username and password')
        return super().form_invalid(form)
    


def signout(request):
    logout(request)
    return redirect('signin')

def profile(request):
    if request.user.is_authenticated:
        purchased_cars = request.user.purchased_cars.all()
        return render(request, 'profile.html', {'purchased_cars': purchased_cars})
    else:
        return redirect('signin')


def change_password(request):
    if request.method == 'POST':
        form = SetPasswordForm(user=request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Changed successfully')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


def change_profile(request):
    if request.method == 'POST':
        form = ChangeUserData(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')
            form = ChangeUserData()
        else:
            messages.error(request, 'There was an error creating your account')
    else:
        form = ChangeUserData(instance = request.user)

    return render(request, 'change_profile.html', {'form': form,})