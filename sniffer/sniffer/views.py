from django.shortcuts import render
from . import http_sniffer


# Create your views here.
def index(request):
    print(request)
    if (request.GET.get('search_btn')):
        # MACOS = en0
       http_sniffer.sniff_packet('en0')

    return render(request, "index.html")
