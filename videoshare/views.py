from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Profile, Like, Dislike, CustomUser

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts':post})

def likepost(request):
    user = request.user
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    like_filter = Like.objects.filter(post=post_id, user=user).first()

    if like_filter is None:
        new_like = Like.objects.create(post=post_id, user=user)
        new_like.save()
        post.like_count = int(post.like_count)+ 1
        post.save()
        return redirect('index')
    else:
        like_filter.delete()
        post.like_count = int(post.like_count) - 1
        post.save()
        return redirect('index')

def dislikepost(request):
    user = request.user
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    dislike_filter = Dislike.objects.filter(post=post_id, user=user).first()

    if dislike_filter is None:
        new_dislike = Dislike.objects.create(post=post_id, user=user)
        new_dislike.save()
        post.dislike_count = int(post.dislike_count)+ 1
        post.save()
        return redirect('index')
    else:
        dislike_filter.delete()
        post.dislike_count = int(post.dislike_count) - 1
        post.save()
        return redirect('index')
def viewcount(request):
    pass
    

def detail(request, id):
    like = Like.objects.filter(post=id)
    dislike = Dislike.objects.filter(post=id)

    post = Post.objects.get(id=id)
    user1= CustomUser.objects.get(email=post.user)
    user = Profile.objects.get(user=user1)

    return render(request, 'postdetail.html', {'user':user,'likes':like, 'dislikes':dislike})

@login_required
def post(request):
    if request.method=='POST':
        user= request.user
        description = request.POST['dscription']
        video_link = request.POST['link']

        if len(description)==0 or len(video_link)==0:
            messages.info(request, 'Any field is empty')
            return redirect('post')
        po = Post(user=user, postdescription=description, video_link=video_link)
        po.save()
        return redirect('index')
    return render(request, 'post.html')
