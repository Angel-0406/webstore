from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mebellar,Bolim,Postlar,Izohlar
from .forms import ContactForm,ProfileForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def Malumot(request):
    return render(request, "Ma'lumot.html")


def Jihozlar(request):
    mebelllar = Mebellar.objects.all()
    context = {'mebelllar': mebelllar}
    return render(request, "Mebellar.html",context)


def Boglanish(request):
    return render(request, "Bog'lanish.html")


def Bolak(request):
    bolimlar=Bolim.objects.all()
    context = {'bolimlar': bolimlar}
    return render(request, "Bo'lim.html",context)

def asos(request):
    asosi=Postlar.objects.all()
    context = {'asosi': asosi}
    return render(request,"base.html",context)
def Izoh(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Izohlar.objects.create(**data)
            return redirect("index")
    context = {'form': form}
    return render(request,"Bog'lanish.html",context)
def kirish(request):
    return render(request, "kirish.html")
def parol(request):
    return render(request, "parol.html")
def Profil(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            # print(username)
            # print(password)
            if user is not None:
                login(request, user)
                # first_name=form.cleaned_data['first_name']
                # last_name=form.cleaned_data['last_name']

                return redirect('index')
                # return render(request,'kirish.html',context)
            else:
                data = {
                    'form': form,
                    'message': "Parol xato! Qayta ro'yhatdan o'tmoqchi bo'lsangiz 'Parolingizni unutdingizmi'ni bosing"
                }
                return render(request, 'kirish.html', data)
        else:
            return HttpResponse("Xato ko'rsatkichlar kiritildi")
    else:
        form = ProfileForm()
        context = {'form': form}
        return render(request, 'kirish.html', context)

