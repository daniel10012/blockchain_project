from django.contrib import admin

from .models import Data, Block, Blockchain

admin.site.register(Data)
admin.site.register(Block)
admin.site.register(Blockchain)