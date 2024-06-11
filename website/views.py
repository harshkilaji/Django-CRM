from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AddRecord
from .models import Record
from django.db.models import Q

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.error(request, 'Wrong Email or Password, please try again...')
            return redirect('home')
    
    if request.user.is_authenticated:
        query = request.GET.get('q')
        if query:
            records = Record.objects.filter(
                Q(user=request.user) & 
                (Q(name__icontains=query) | Q(alias__icontains=query) | Q(description__icontains=query) | 
                 Q(powers__icontains=query) | Q(city__icontains=query) | Q(status__icontains=query))
            )
        else:
            records = Record.objects.filter(user=request.user)
    else:
        records = []
    
    return render(request, 'website/home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully...')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "User created and logged in successfully!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'website/register.html', {'form': form})

@login_required
def records(request, pk):
    rec = get_object_or_404(Record, pk=pk, user=request.user)
    return render(request, 'website/record.html', {'rec': rec})

@login_required
def delete_record(request, pk):
    rec = get_object_or_404(Record, pk=pk, user=request.user)
    rec.delete()
    messages.success(request, "Record deleted successfully...")
    return redirect('home')

@login_required
def add_record(request):
    if request.method == 'POST':
        form = AddRecord(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            messages.success(request, "Record added successfully!")
            return redirect('home')
    else:
        form = AddRecord()
    return render(request, 'website/add_record.html', {'form': form})

@login_required
def update(request, pk):
    rec = get_object_or_404(Record, pk=pk, user=request.user)
    form = AddRecord(request.POST or None, instance=rec)
    if form.is_valid():
        form.save()
        messages.success(request, "Update successful!")
        return redirect('home')
    return render(request, 'website/update.html', {'form': form})
