from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from  django.forms import formset_factory


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class SignUp(generic.CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def home(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            genres = "|".join(sorted(form.cleaned_data['categories']))
            movies = []
            for e in Movies.objects.filter(genres=genres):
                movies.append(e.title)
            request.session['movies'] = movies
            return HttpResponseRedirect('/nxtwatch/play')
    else:
        form = CategoryForm()
    return render(request, 'home.html', {'form': form})

def play(request):
    movies = request.session.get('movies')
    #print(request.session.get('movies'))
    RatingFormSet = formset_factory(RatingForm, extra=2)
    formset = RatingFormSet()
    return render(request,'nxtwatch/play.html', {'movies': movies, 'formset':formset})
