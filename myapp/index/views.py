from django.shortcuts import render
# from datetime import datetime

# now = datetime.datetime.now()

# Create your views here.
def index_index(request):
    return render(request, "index/index.html")

def index_about(request):
    return render(request, "index/about.html")

def index_contact(request):
    return render(request, "index/contact.html")

def index_home(request):
    # current_time = datetime.now().time() 
    return render(request, "index/home.html")#, {'current_time':current_time} )

def index_location(request):
    return render(request, "index/location.html")

def index_links(request):
    return render(request, "index/links.html")

def index_server(request):
    return render(request, "index/server.html")

def index_clock(request):
    return render(request, "index/clock.html")