from django.shortcuts import render

posts = [
    {
        'author':'Lin Shan',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '29/10/2020'
    },
    {
        'author':'LS',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '30/10/2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'title':'home',
        'posts':posts,
    }
    return render(request,'blog/home.html', context)

def about(request):
    context = {
        'title':'about',
    }
    return render(request,'blog/about.html', context)
