from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from clients.models import Client

def index(request):
    clients = Client.objects.order_by('name')

    data = {
        'clients': clients
    }

    return render_to_response(
        'clients/index.html',
        data,
        context_instance=RequestContext(request)
    )

def detail(request, slug):
    client = get_object_or_404(Client, slug=slug)
    records = client.record_set.order_by('file_no')

    data = {
        'client': client,
        'records': records
    }

    return render_to_response(
        'clients/detail.html',
        data,
        context_instance=RequestContext(request)
    )
    
