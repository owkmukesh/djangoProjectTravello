from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):
    dest1=Destination()
    dest1.name="Hyderabad"
    dest1.price=800
    dest1.desc="Biryani First, Sherwani next"
    dest1.img="static/img/place/1.png"

    dest2=Destination()
    dest2.name="Mumbai"
    dest2.price=1000
    dest2.desc="The city never sleeps"
    dest2.img="static/img/place/2.png"

    dest3=Destination()
    dest3.name="Benguluru"
    dest3.price=900
    dest3.desc="Industrial Area"
    dest3.img="static/img/place/3.png"

    dests=[dest1,dest2,dest3]
    return render(request,"index.html",{"dests":dests})