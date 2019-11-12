from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from  django.forms import formset_factory
import time


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
            existingRatings = Ratings.objects.filter(userid=request.user.id).values_list('movieid',flat=True)
            for e in Movies.objects.filter(genres=genres).exclude(movieid__in = existingRatings):
                temp = {}
                temp["movieid"] = e.movieid
                temp["title"] = e.title
                movies.append(temp)
            request.session['movies'] = movies
            return HttpResponseRedirect('/nxtwatch/play')
    else:
        form = CategoryForm()
    return render(request, 'home.html', {'form': form})

def play(request):
    movies = request.session.get('movies')
    print(len(movies),request.user.id)
    RatingFormSet = formset_factory(RatingForm)
    formset = RatingFormSet(initial=[{'title':movie["title"], 'movieid': movie["movieid"] } for movie in movies])
    formset.extra -= 1
    if request.method == 'POST':
       filled_formset = RatingFormSet(request.POST)
       for form in filled_formset:
           if form.is_valid():
               ratingObj = Ratings()
               ratingObj.userid = request.user.id
               ratingObj.movieid = form.cleaned_data["movieid"]
               ratingObj.rating = form.cleaned_data["rating"]
               ratingObj.timestamp = int(time.time())
               ratingObj.save()
       return HttpResponseRedirect('/nxtwatch/results')
    return render(request,'nxtwatch/play.html', {'formset':formset})

def results(request):
    return render(request,'nxtwatch/results.html')
