from django.shortcuts import render, redirect
from django_pandas.io import read_frame
import pandas as pd

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
            if len(movies) > 10:
                request.session['movies'] = movies[:10]
            else:
                request.session['movies'] = movies
            return HttpResponseRedirect('/nxtwatch/play')
    else:
        form = CategoryForm()
    return render(request, 'home.html', {'form': form})

def play(request):
    movies = request.session.get('movies')
    #print(len(movies),request.user.id)
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
    movies = Movies.objects.all()
    movies_df = read_frame(movies)
    ratings = Ratings.objects.all()
    ratings_df = read_frame(ratings)
    data = pd.merge(movies_df, ratings_df, on="movieid")
    # creating dataframe with 'rating' count values 
    ratings = pd.DataFrame(data.groupby('title')['rating'].mean())  
    ratings['num of ratings'] = pd.DataFrame(data.groupby('title')['rating'].count()) 
    moviemat = data.pivot_table(index ='userid', columns ='title', values ='rating')
    ratings.sort_values('num of ratings', ascending = False).head(10) 
    currently_rated_movies = request.session.get('movies')
    results = {}
    for item in currently_rated_movies:
        # analysing correlation with similar movies 
        _user_ratings = moviemat[item["title"]]
        similar_to_ = moviemat.corrwith(_user_ratings) 
        corr_ = pd.DataFrame(similar_to_, columns =['Correlation']) 
        corr_.dropna(inplace = True) 
        # Similar movies like current title 
        corr_.sort_values('Correlation', ascending = False).head(10)
        corr_ = corr_.join(ratings['num of ratings']) 
        strongest_corr = corr_[corr_['num of ratings']>100].sort_values('Correlation', ascending = False).head(1)
        strongest_corr = strongest_corr.rename(columns = {"num of ratings": "no_of_ratings"})
        if not strongest_corr.empty:
            results[strongest_corr.index.values[0]] = Ratings.objects.filter(userid=request.user.id).filter(movieid=item["movieid"]).values_list('rating',flat=True)[0] * strongest_corr.Correlation[0] * strongest_corr.no_of_ratings[0]
    
    print(results)
    return render(request,'nxtwatch/results.html', {'results':results})