from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Data
from django.urls import reverse
from .forms import NewhashForm


def data(request):
    data = Data.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'hash/data.html', context)

def single(request,data_id):
    single_data = Data.objects.get(id=data_id)
    context = {
        'single_data': single_data,
    }
    return render(request, 'hash/single.html', context)

def get_hash(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewhashForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewhashForm()

    return render(request, 'hash/new.html', {'form': form})