from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from .models import Data, Block, Blockchain
from django.urls import reverse
from .forms import NewhashForm, NewblockForm, MineForm, GenesisForm
from datetime import datetime


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
        form = NewhashForm(request.POST, initial={'h': "0"})
        # check whether it's valid:
        if form.is_valid():
            data = Data(content=form.cleaned_data['data'])
            hash = data.hash()
            context = {
                'data': data,
                'hash':hash,
            }

            form = NewhashForm(initial={'data': data, 'h': hash})

            return render(request, 'hash/new.html', {'form': form})

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
        form = NewblockForm(request.POST, initial={'h': "0"})
        # check whether it's valid:
        if form.is_valid():
            block = Block(block_num=form.cleaned_data['block_num'],
                          nonce=form.cleaned_data['nonce'],
                          data=form.cleaned_data['data'])
            #block.save
            block_num = block.block_num
            nonce = block.nonce
            data = block.data

            h = block.hashing()

            context = {
                'block_num':block_num,
                'nonce':nonce,
                'data': data,
                'h':h,
            }

            form = NewblockForm(initial={'block_num': block_num, 'nonce': nonce, 'data': data, 'h': h})

            return render(request, 'hash/block.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewblockForm()
        print("ddddd")

    return render(request, 'hash/block.html', {'form': form})



def mine(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("eeee")
        # create a form instance and populate it with data from the request:
        form = MineForm(request.POST, initial={'h': "0","previous_h": "0"*64, 'timestamp': str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))})
        # check whether it's valid:
        if form.is_valid():
            block = Block(
                          block_num=form.cleaned_data['block_num'],
                          nonce="0",
                          data=form.cleaned_data['data'],
                          timestamp=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                            )
            #block.save()
            block_num = block.block_num
            nonce = block.nonce
            data = block.data
            timestamp=block.timestamp

            dict = block.mine()
            print(dict)
            h4 = dict["hash"][:4]
            print(h4)

            # context = {
            #     'block_num':block_num,
            #     'nonce':dict["nonce"],
            #     'h':dict["hash"],
            #     'data': data,
            #     'timestamp': timestamp,
            # }

            form = MineForm(initial={'block_num':block_num,
                                     'nonce':dict["nonce"],
                                     'data': data,
                                     'timestamp': timestamp,
                                     "previous_h": "0"*64,
                                     'h':dict["hash"]})


            return render(request, 'hash/mine.html', {'h4':h4,'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MineForm()
        print("ffff")

    return render(request, 'hash/mine.html', {'form': form})


def blockchain(request):

    blockchain_0 = Blockchain(chain_num="0")
    genesis_block = Block(block_num = "0",
                            nonce = "0",
                            data = "Genesis Block",
                            timestamp = "2019-05-01 00:00:00",
                            hash = "0",
                            previous_hash = "0",
                            blockchain = blockchain_0,)
    genesis_block.save()

    form0 = GenesisForm(initial={'block_num': genesis_block.block_num,
                             'nonce': genesis_block.nonce,
                             'data': genesis_block.data,
                             'timestamp': genesis_block.timestamp,
                             "previous_h": genesis_block.previous_hash,
                             'h': genesis_block.hash})

    form_dict = {}
    form_dict["form0"]=form0


    lenght_blockchain = (len(blockchain_0.chain()))



    for i in range(1,lenght_blockchain):
        #print(str(i))
        # if str(i) in request.POST:
        #     print("YOOOOOOOOO")

        if request.method == 'POST':

            current_form = MineForm(initial={'block_num':str(i),
                                         'timestamp': "timestamp",
                                         "previous_h":"yo",
                                         'h':"666"})

            if current_form.is_valid():
                block = Block(
                    block_num=current_form.cleaned_data['block_num'],
                    nonce="0",
                    data=current_form.cleaned_data['data'],
                    timestamp=str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                )


                form_dict[f"form{i}"] = current_form

                form_dict["forms"] = form_dict
                #print(form_dict)
                return render(request, 'hash/blockchain.html', form_dict)
            #return JsonResponse(blockchain_0.chain(), safe=False)

        else:
            for i in range(1, lenght_blockchain):
                current_form = MineForm(initial={'block_num': str(i),
                                                 'timestamp': "timestamp",
                                                 "previous_h": "yo",
                                                 'h': "666"})
                form_dict[f"form{i}"] = current_form

            form_dict["forms"] = form_dict
            print(form_dict)
            return render(request, 'hash/blockchain.html', form_dict)

