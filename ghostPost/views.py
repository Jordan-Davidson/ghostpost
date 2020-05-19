from django.shortcuts import render, reverse, HttpResponseRedirect
from ghostPost.models import RoastBoast
from ghostPost.forms import addRoastBoast

# Create your views here.
def index(request):
    html = 'index.html'
    data = RoastBoast.objects.order_by('-time')
    return render(request, html, {'data': data})

def roast(request):
    html = 'index.html'
    data = RoastBoast.objects.filter(roastBoast=True).order_by('-time')
    return render(request, html, {'data': data})

def boast(request):
    html = 'index.html'
    data = RoastBoast.objects.filter(roastBoast=False).order_by('time')
    return render(request, html, {'data': data})

def posts(request, id):
    html = 'post.html'
    data = RoastBoast.objects.filter(id=id)[0]
    return render(request, html, {'data': data})

def upvote(request, id):
    post = RoastBoast.objects.get(id=id)
    post.upvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('sort', kwargs={'id': id}))

def downvote(request, id):
    post = RoastBoast.objects.get(id=id)
    post.downvotes += 1
    post.save()
    return HttpResponseRedirect(reverse('sort', kwargs={'id': id}))


def sort(request, id):
    post = RoastBoast.objects.get(id=id)
    post.score = post.upvotes - post.downvotes
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def top(request):
    html = 'index.html'
    data = RoastBoast.objects.all().order_by('-score')
    return render(request, html, {'data': data})

def addRB(request):
    html = 'form.html'
    if request.method == 'POST':
        form = addRoastBoast(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            RoastBoast.objects.create(
                roastBoast = data['roastBoast'],
                post = data['post']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = addRoastBoast()
    return render(request, html, {'form': form})