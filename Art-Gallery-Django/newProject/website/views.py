from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Collection

def home(request):
  records = Collection.objects.all()
  # check if the person is logged in
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Logged in')
      return redirect('home')
    else:
      messages.success(request, 'There is some error logging in, please try again.')
      return redirect('home')
  else:
    return render(request, 'home.html', {'records': records})

def logout_user(request):
  logout(request)
  messages.success(request, 'Logged out')
  return redirect('home')

def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(request, username=username, password=password)
      login(request, user)
      messages.success(request, 'Registration successful.')
      return redirect('home')
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form': form})
  return render(request, 'register.html', {'form': form})

def art_record(request, pk):
  if request.user.is_authenticated:
    record = Collection.objects.get(id=pk)
    return render(request, 'record.html', {'record': record})
  else:
    messages.success(request, 'Please log in to view the page.')
    return redirect('home')

def delete_record(request, pk):
  if request.user.is_authenticated:
    record_to_be_deleted = Collection.objects.get(id=pk)
    record_to_be_deleted.delete()
    messages.success(request, 'Record deleted.')
    return redirect('home')
  else:
    messages.success(request, 'Please log in for the action.')
    return redirect('home')

def add_record(request):
  form = AddRecordForm(request.POST or None)
  if request.user.is_authenticated:
    if request.method == 'POST':
      if form.is_valid():
        form.save()
        messages.success(request, 'Art adding successful.')
        return redirect('home')
    else:
      return render(request, 'add.html', {'form': form})
  else:
    messages.success(request, 'Please log in for the action.')
    return redirect('home')

def update_record(request, pk):
  if request.user.is_authenticated:
    record_to_be_updated = Collection.objects.get(id=pk)
    form = AddRecordForm(request.POST or None, instance=record_to_be_updated)# pass in instance of current record
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated.')
        return redirect('home')
    else:
      return render(request, 'update.html', {'form': form})
  else:
    messages.success(request, 'Please log in for the action.')
    return redirect('home')