from django.shortcuts import render
from .models import HomeText
from posts.models import Post

# Create your views here.
def home(request):
    homepara = HomeText.objects
    home_posts = Post.objects.all()[:3]
    context = {'homepara': homepara, 'home_posts': home_posts}
    return render(request, 'landing/home.html', context)

def about(request):
    return render(request, 'landing/about.html')
    
def contact(request):
    return render(request, 'landing/contact.html')
