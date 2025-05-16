from django.shortcuts import render
from .models import BlogPost, Question, Profile, Video

def home(request):
    profiles = Profile.objects.all()  # Fetch profile images
    videos = Video.objects.all()  # Fetch videos
    return render(request, 'website/home.html', {'profiles': profiles, 'videos': videos})

def blog(request):
    posts = BlogPost.objects.all()
    return render(request, 'website/blog.html', {'posts': posts})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        question = request.POST.get('question')
        Question.objects.create(name=name, question=question)
    return render(request, 'website/contact.html')

def about(request):
    return render(request, 'website/about.html')
