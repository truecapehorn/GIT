from django.shortcuts import render
from .models import Database
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


#def baza(request):
#    data = Database.objects.all()
#    print(data)
#    return render(request, 'baza/index.html', {'data': data})

class BazaView(ListView):
    queryset = Database.objects.all()
    context_object_name = 'baza'
    paginate_by = 2
    template_name = 'baza/index.html'
