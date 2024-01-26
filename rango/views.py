from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #Return a rendered response to send to the client.
    return render(request, 'rango/index.html', context=context_dict)
    #create a string containing the hyperlink to the about page
    #link_to_about = '<a href="/rango/about/">About</a>'
    #add the hyperlink to the HttpResponse
    #return HttpResponse("Rango says hey there partner! "+ link_to_about)
    


def about(request):
    # If you're not using a template, keep the HttpResponse as is:
    link_to_index = '<a href="/rango/">Index</a>'
    return HttpResponse("Rango says here is the about page. " + link_to_index)