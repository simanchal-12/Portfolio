from django.http import HttpResponse
from django.shortcuts import render,HttpResponse
from.models import Home,About,Profile,Skills,Portfolio,Category

# Create your views here.
def index(request):
    #Home
    home=Home.objects.latest('updated')
    
    #About
    about=About.objects.latest('updated')
    profiles=Profile.objects.filter(about=about)
    
    #Skills
    categories=Category.objects.all()
    
    #Portfolio
    portfolios=Portfolio.objects.all()
    
    context={
        'home':home,
        'about':about,
        'profiles':profiles,
        'categories':categories,
        'portfolios':portfolios,
        
        
    }
    return render(request,"home.html",context)