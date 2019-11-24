from django.shortcuts import render
from django.http import HttpResponse
from . import mydir as md

# Create your views here.

def home_view(request, *args, **kwargs):
    item1 = ''
    item2 = ''
    dealername = ''
    context = {}
    if request.method == "POST":  
        dealername = request.POST.get('dealername')
        folder = dealername[0].upper()
        item1 = f'Directory created in /installs/{folder}/{dealername}'
        md.make_folder(dealername)
        context = {
            'item1': item1,
            'item2': item2
        }
    return render(request, "md/mdform.html", context)