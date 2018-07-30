from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Entry

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('artist_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})