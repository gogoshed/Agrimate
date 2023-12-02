# forum/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Thread, Post
# from .forms import ThreadForm, PostForm



# forum/views.py
from django.shortcuts import render, get_object_or_404
from .models import Thread, Post

def forum_index(request):
    threads = Thread.objects.all()
    return render(request, 'forum/forum_index.html', {'threads': threads})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts})

def forum(request):
    return render(request, 'forum/templates/forum/forum_index.html', {})


@login_required
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.creator = request.user
            thread.save()
            return redirect('forum_index')
    else:
        form = ThreadForm()

    return render(request, 'forum/create_thread.html', {'form': form})

@login_required
def create_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.creator = request.user
            post.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = PostForm()

    return render(request, 'forum/create_post.html', {'form': form, 'thread': thread})
