from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Data, Block
from django.urls import reverse
from .forms import NewhashForm, NewblockForm


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
        print("aaaa")
        # create a form instance and populate it with data from the request:
        form = NewhashForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = Data(content=form.cleaned_data['data'])
            hash = data.hash()
            context = {
                'data': data,
                'hash':hash,
            }
            print(data)
            print(hash)
            return render(request, 'hash/new.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewhashForm()
        print("bbbbb")

    return render(request, 'hash/new.html', {'form': form})


def get_block(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("cccc")
        # create a form instance and populate it with data from the request:
        form = NewblockForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            block = Block(block_num=form.cleaned_data['block_num'], nonce=form.cleaned_data['nonce'], data=form.cleaned_data['data'])

            h = block.hashing()

            context = {
                'block_num':block_num,
                'nonce':nonce,
                'data': data,
            }
            print(type(block_num))
            print(nonce)
            print(h)


            return render(request, 'hash/block.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewblockForm()
        print("ddddd")

    return render(request, 'hash/block.html', {'form': form})