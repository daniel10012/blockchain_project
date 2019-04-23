from django.urls import path

from . import views

app_name = "hash"

urlpatterns = [
    path('', views.data, name='data'),
    path('<int:data_id>/', views.single, name='single'),
    path('new/', views.get_hash, name='get_hash'),
    path('block/', views.get_block, name='get_block'),
    path('mine/', views.mine, name='mine'),
]

