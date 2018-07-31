from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Entry

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from rest_framework import generics
# from .serializers import entrieserializer
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('gratitude_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def entry_list(request):
    entries = Entry.objects.all().values()
    entries_list = list(entries)
    return JsonResponse(entries_list, safe=False)

def entry_detail(request, pk):
    entry = Entry.objects.get(id=pk).values()
    return JsonResponse(entry, safe=False)

# @login_required
def entry_create(request):
    if request.is_ajax():
        if request.method == 'POST':
            entry = request.body.save()
            # form = entryForm(request.POST)
            # if form.is_valid():
            #     entry = form.save()
            return redirect('entry_detail', pk=entry.pk)
        # else:
        #     form = entryForm()
        # return render(request, 'gratitude/entry_form.html', {'form': form})
        return HttpResponse("OK")

# @login_required
def entry_edit(request, pk):
    entry = Entry.objects.get(pk=pk)
    if request.method == "POST":
        form = entryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save()
            return redirect('entry_detail', pk=entry.pk)
    else:
        form = entryForm(instance=entry)
    return render(request, 'gratitude/entry_form.html', {'form': form})


# @login_required
def entry_delete(request, pk):
    Entry.objects.get(id=pk).delete()
    return redirect('entry_list')











# class EntryList(generics.ListCreateAPIView):
#     queryset = Entry.objects.all()
#     serializer_class = entrieserializer
    

# class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Entry.objects.all()
#     serializer_class = entrieserializer


# def entries_list(request):
#     """
#     Returns Json list of all restaurants
#     """
#     if request.method == "GET":
#         rest_list = Restaurant.objects.order_by('-pub_date')
#         serializer = RestaurantSerializer(rest_list, many=True)
#         return JsonResponse(serializer.data, safe=False)