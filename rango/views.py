from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #create a string containing the hyperlink to the about page
    link_to_about = '<a href="/rango/about/">About</a>'
    #add the hyperlink to the HttpResponse
    return HttpResponse("Rango says hey there partner! "+ link_to_about)

def about(request):
    link_to_index = '<a href="/rango/">Index</a>'
    return HttpResponse("Rango says here is the about page. " + link_to_index)