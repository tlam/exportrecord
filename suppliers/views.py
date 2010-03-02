from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from suppliers.models import Supplier

def index(request):
    suppliers = Supplier.objects.order_by('name')

    data = {
        'suppliers': suppliers
    }

    return render_to_response(
        'suppliers/index.html',
        data,
        context_instance=RequestContext(request)
    )

def detail(request, slug):
    supplier = get_object_or_404(Supplier, slug=slug)
    records = supplier.record_set.order_by('file_no')

    data = {
        'client': supplier,
        'records': records
    }

    return render_to_response(
        'clients/detail.html',
        data,
        context_instance=RequestContext(request)
    )
