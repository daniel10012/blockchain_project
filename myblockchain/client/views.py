from django.http import HttpResponse
from .models import Blockchain
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

blockchain = Blockchain()

def index(request):
    return render(request, 'client/base.html')

#@app.route('/chain', methods=['GET'])

def full_chain(request):
    context = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return render(request, 'client/chain.html', context)