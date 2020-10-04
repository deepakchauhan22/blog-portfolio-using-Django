from django.shortcuts import render,get_object_or_404
from .models import Port

# Create your views here.
def home(request):
    ports = Port.objects
    return render(request, 'home.html', {
        'ports' : ports
    })
def detail (request, port_id):
    port_detail = get_object_or_404(Port, pk=port_id)
    return render(request, 'detail.html',{
        'port': port_detail
    })
