from django.shortcuts import render
from .models import Row
from django.shortcuts import get_object_or_404
from django.views.generic import ListView


# TODO: Dodac widoki: deail reckord
# TODO: Dodac widoki: filtrownia po rekordach. Post.objects.all().order_by('created_date'),
# TODO: Dodac widoki: przeszukiwania, A gdybyśmy chciały wyświetlić wszystkie wpisy zawierające słowo 'title' w polu tytuł? Post.objects.filter(title__contains = 'tytuł')
# TODO: Zmienić backgroud na ciemny.

class RowsView(ListView):
    queryset = Row.objects.all()
    context_object_name = 'row_list'
    paginate_by = 100
    template_name = 'kartoteka/row_list.html'


def row_detail(request, pk):
    row = get_object_or_404(Row, pk=pk)
    return render(request, 'kartoteka/row_detail.html', {'row': row})
