from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm


# Create your views here.
def index(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "index.html", {"tweets": tweets})

def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("index")
    else:
        form = TweetForm()
    
    return render(request, "tweet_create.html", {"form": form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("index")
    else:
        form = TweetForm(instance=tweet)
    
    return render(request, "tweet_edit.html", {"form": form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("index")
    return render(request, "tweet_delete.html", {"tweet": tweet})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})