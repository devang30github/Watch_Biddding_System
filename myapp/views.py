# Create your views here.
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.db.models import Max
from django.utils import timezone
from .forms import UserRegistrationForm, UserLoginForm
from .forms import WatchForm, BidForm
from .models import Watch, Bid
from django.db.models import F, Value, Case, When, DecimalField



def index(request):
    return render(request, 'index.html')

def home(request):
    top_watches = Watch.objects.order_by('-current_bid')[:3]
    return render(request, 'home.html', {'top_watches': top_watches})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')


@login_required
def add_watch(request):
    if request.method == 'POST':
        form = WatchForm(request.POST, request.FILES)
        if form.is_valid():
            watch = form.save(commit=False)
            watch.owner = request.user
            watch.save()
            return redirect('list_watches')
    else:
        form = WatchForm()
    return render(request, 'add_watch.html', {'form': form})

@login_required
def list_watches(request):
    watches = Watch.objects.all()
    return render(request, 'list_watches.html', {'watches': watches})

@login_required
def place_bid(request, watch_id):
    watch = get_object_or_404(Watch, pk=watch_id)
    
    if request.user == watch.owner:
        starting_bid = watch.starting_bid
    else:
        starting_bid = watch.current_bid
    
    if timezone.now() > watch.bid_end_date:
        messages.error(request, "Bidding for this watch has ended.")
        return redirect('list_watches')

    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid_amount = form.cleaned_data['amount']
            if bid_amount >= starting_bid:
                bid = form.save(commit=False)
                bid.watch = watch
                bid.bidder = request.user
                bid.save()
                watch.current_bid = bid_amount
                watch.save()
                return redirect('list_watches')
            else:
                messages.error(request, "Your bid must be greater than or equal to the starting bid.")
    else:
        form = BidForm()
    
    return render(request, 'place_bid.html', {'form': form, 'watch': watch})

@login_required
def user_profile(request):
    user_bids = Bid.objects.filter(bidder=request.user).select_related('watch').order_by('-bid_time')
    return render(request, 'user_profile.html', {'user_bids': user_bids})


