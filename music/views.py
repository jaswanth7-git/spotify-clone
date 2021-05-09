from django.shortcuts import HttpResponse, render
from .models import *

# Create your views here.
def vamshi(request):
    return render (request, 'music/home.html')



def vardhan(request):
    albums= Album.objects.all()
    

    return render(request,'music/vardhan.html', {'albums':albums} )


def jaswanth(request, pk):
    albums= Album.objects.get(id=pk)

    context = {'albums':albums}
    
    return render (request, 'music/songs.html', context)

def contact(request):
    return render(request, 'music/contact.html')