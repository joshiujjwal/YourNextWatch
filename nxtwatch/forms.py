from django import forms

class CategoryForm(forms.Form):
    OPTIONS = {
        ("Action","Action"),
        ("Adventure","Adventure"),
        ("Animation","Animation"),
        ("Children's","Children's"),
        ("Comedy","Comedy"),
        ("Crime","Crime"),
        ("Documentary","Documentary"),
        ("Drama","Drama"),
        ("Film-Noir","Film-Noir"),
        ("Horror","Horror"),
        ("Musical","Musical"),
        ("Mystery","Mystery"),
        ("Romance","Romance"),
        ("Sci-Fi","Sci-Fi"),
        ("Thriller","Thriller"),
        ("War","War"),
        ("Western","Western"),
    }
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=OPTIONS)

class RatingForm(forms.Form):
    CHOICES=[('1','1'),
        ('1.5','1.5'),
        ('2','2'),
        ('2.5','2.5'),
        ('3','3'),
        ('3.5','3.5'),
        ('4','4'),
        ('4.5','4.5'),
        ('5','5'),]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    movieid = forms.IntegerField(widget = forms.HiddenInput(), required = False)
    title = forms.CharField(required = False, widget=forms.TextInput(attrs={'readonly':'readonly'}))