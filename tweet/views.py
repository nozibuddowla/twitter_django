from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
import logging
from django.core.paginator import Paginator

# Create your views here.
logger = logging.getLogger(__name__)

def index(request):
    search_query = request.GET.get('search', '').strip()
    logger.debug(f"Searched Query for: {search_query}")

    tweets = Tweet.objects.filter(text__icontains=search_query).order_by('-created_at') if search_query else Tweet.objects.all().order_by('-created_at')


    paginator = Paginator(tweets, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    logger.info(f"User '{request.user}' searched for '{search_query}'. Found {tweets.count()} tweets.")

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = TweetForm(request.POST, request.FILES)
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                return redirect('index')
        else:
            return redirect('login')
    else:
        form = TweetForm()
    
    return render(request, "index.html", {"tweets": tweets, "form": form, "page_obj": page_obj, "search_query": search_query})


@login_required
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

@login_required
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

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("index")
    return render(request, "tweet_delete.html", {"tweet": tweet})

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    else:
        form = UserRegistrationForm()
    
    return render(request, "registration/register.html", {"form": form})
