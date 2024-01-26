# FiveLakes views
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from managers.models import CustomUser

User = get_user_model()

def index(request):
    context = {}
    if request.user.is_authenticated:
        return redirect(reverse_lazy('states'))
    else:
        return redirect(reverse_lazy('login'))
    # return render(request, 'template/index.html')

# ERROR PAGES
def PageNotFound(request):
    return render(request, 'template/404.html')

def admin_error(request):
    return render(request, 'template/404.html')

# REGISTRATION VIEWS
class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('client_begin1')

    def form_valid(self, form):
        form.save()
        email = self.request.POST['email']
        password = self.request.POST['password1']
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)


def password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
    return render(request, 'registration/password_reset_form.html', {'form': form})
    # return render(request, 'registration/password_reset_form.html')