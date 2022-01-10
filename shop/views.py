from django.contrib.auth.decorators import login_required
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post,Categories
from django.db.models import Q
from django.views.generic import ListView,DetailView

# Create your views here.


#list view for the home page 
class PostListView(ListView):
   model= Post
   template = 'shop/index.html'
   context_object_name = 'items'  
   ordering = ['published_date']


#the same thig but with method 
def index(request):
   context = Categories.objects.all()
   items = Post.objects.all()
   return render(request,'shop/home.html',{'categories': context,'items' : items })



class PostDetailView(DetailView):
   model = Post
   template = 'shop/detail.html'
   context_object_name = 'post'


def privacy_policy(request):
       return render(request,'shop/policy.html')

def about(request):
   return render(request,'shop/about.html');

def about(request):
       return render(request,'shop/detail.html');



# query the search results
def search_venues(request):
   searched = request.POST['searched']
   venues = Post.objects.filter(Q(title__contains=searched) | Q(description__contains=searched) )
   result = { 'searched' : searched, 'venues': venues }

   if request.method == 'POST':
      return render(request,'shop/search_venues.html',result)
   else:
      return render(request,'shop/search_venues.html')
   
@login_required
def post_ad(request):
   return render(request,'shop/post_ad.html')