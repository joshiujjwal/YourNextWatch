from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CategoryForm
from .models import Movies
from django.http import HttpResponseRedirect
from  django.forms import formset_factory


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def home(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,'nxtwatch/play.html', {'category': form.cleaned_data})
    else:
        form = CategoryForm()
    return render(request, 'home.html', {'form': form})

def play(request):
    return render(request,'nxtwatch/play.html')
