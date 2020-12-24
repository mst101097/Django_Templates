from django.http import HttpResponse
from django.shortcuts import render


def home_view(request ,*args , **kwargs):
    # print(args,kwargs)
    # print(request.user)
    return render(request,"home.html",{})

def contact_view(request,*args , **kwargs):
    return render(request,"contact.html",{})

def about_view(request,*args , **kwargs):
    my_context = {
        "mytext" :"this is about us page ",
        "my_num" : " this is my no 12342 ",
        "mylist":[233,45,35,654,"abd"],
        "myhtml": "<h1>MohitSingh</h1>"
    }
    return render(request,"about.html",my_context)

def social_view(request,*args , **kwargs):
    return render(request,"social.html",{})
