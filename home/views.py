from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable1':'GUDELLI',
        'variable2':'SAI DHEERAJ'
    }
    return render(request,"index.html",context)
    #return  HttpResponse("this is http response")
    
def about(request):
    return  HttpResponse("this is about response")
def services(request):
    return  HttpResponse("this is services response")
def contact(request):
    return  HttpResponse("this is contact response")
