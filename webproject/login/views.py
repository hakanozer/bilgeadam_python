from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import productService as pro

# Create your views here.
def index(request):
    template = loader.get_template('loginPage.html')
    appTitle = 'Site Title'
    listCity = ["İstanbul","Ankara", "İzmir", "Adana", "Antalya"]
    context = {
        'appTitle': appTitle,
        'listCity': listCity
        }
    return HttpResponse(template.render(context, request))



# user login function
def userLogin(request):
    email = request.POST['email']
    password = request.POST['password']
    if (email == 'ali@mail.com' and password == '12345'):
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        print("Giriş Başarısız")
    return HttpResponseRedirect(reverse('index'))



# open dashboard
def dashboard(request):
    template = loader.get_template('dashboard.html')
    ls = pro.productList()
    context = {
        'productList': ls
    }

    return HttpResponse(template.render(context, request))

