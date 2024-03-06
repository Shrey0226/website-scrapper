from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import link
# Create your views here.


def home(request):
    if request.method == "POST":
        scrap = request.POST.get("input", "")
        site = requests.get(scrap)
        soup = BeautifulSoup(site.text, 'html.parser')

        for links in soup.find_all('a'):
            link_url = links.get('href')
            link_name = links.string
            link.objects.create(link_name=link_name, link_url=link_url)
        return HttpResponseRedirect('/')
    else:
        link_data = link.objects.all()

    return render(request, 'scrape/home.html', {'link_data': link_data})


def delete_link(request):
    x = link.objects.all()
    x.delete()
    return render(request, 'scrape/home.html')
