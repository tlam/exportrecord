from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.shortcuts import redirect, render
from django.template import RequestContext

from export.models import Record
 
def index(request):
    q = ''
    if 'q' in request.GET:
        q = request.GET['q']

    records = Record.objects.filter(
        Q(buyer__name__icontains=q) |
        Q(order_confirm__icontains=q) |
        Q(proforma_invoice__icontains=q) |
        Q(supplier__name__icontains=q)
    ).order_by('file_no')

    data = { 
        'records': records
    }   

    return render(
        request,
        'export/index.html',
        data,
    )   
 
def home_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('export:home')
            else:
                # Return a 'disabled account' error message
                print 'disabled account'
        else:
            # Return an 'invalid login' error message.
            print 'invalid account'

    return render(
        request,
        'export/login.html',
        {},
    )   
