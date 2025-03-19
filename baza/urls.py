
from django.urls import path
from .views import index, Malumot, Jihozlar, Boglanish, Bolak,Izoh,kirish,parol

urlpatterns=[
    path('',index,name='index'),
    path("Ma'lumot",Malumot,name='Malumot'),
    path('Mebellar',Jihozlar,name='Mebellar'),
    path("Bog'lanish",Izoh,name='Boglanish'),
    path("Bo'lim",Bolak,name='Bolim'),
    path('izoh',Izoh,name='Izoh'),
    path('kirish',kirish,name='kirish'),
    path('parol',parol,name='parol'),
]