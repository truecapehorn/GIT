from django.shortcuts import render, get_object_or_404, redirect
from .models import Row
from django.views.generic import ListView
from .forms import RowForm, SearchForm
from django.utils import timezone


# TODO: Dodac widoki: detail reckord
# TODO: Dodac widoki: filtrownia po rekordach. ex.: Post.objects.all().order_by('created_date'),
# TODO: Dodac widoki: przeszukiwania, A gdybyśmy chciały wyświetlić wszystkie wpisy zawierające słowo 'title' w polu tytuł? Row.objects.filter(investor = 'jakias nazwa inwestora')
# TODO: Zmienić backgroud na ciemny.
# TODO: Zrobic oddzielne okno z fromularzami do przeszukiwania , filtrowania rekordów.
# TODO: Zrobic okno ostrzeżeń przy kasowamiu, edytowaniu rekordu.
# TODO: Dodac testy!!!
# TODO: Dodac logowanie . Moze bac jak chris_hawks


class RowsView(ListView):
    queryset = Row.objects.all()
    context_object_name = 'row_list'
    paginate_by = 15
    template_name = 'kartoteka/row_list.html'


class SortView(ListView):  # dodac atrybut co sortujemy
    data = Row.objects.all()
    data = data.extra(select={'sortuj_numerycznie': '(-entry_date+0)'})
    data = data.extra(order_by=['sortuj_numerycznie'])
    queryset = data
    context_object_name = 'sort_list'
    paginate_by = 15
    template_name = 'kartoteka/sort_list.html'


def row_detail(request, pk):
    row = get_object_or_404(Row, pk=pk)
    return render(request, 'kartoteka/row_detail.html', {'row': row})


def row_new(request):
    if request.method == "POST":
        form = RowForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.author = request.user
            row.published_date = timezone.now()
            row.save()
            return redirect('row_detail', pk=row.pk)
    else:
        form = RowForm()
    return render(request, 'kartoteka/row_edit.html', {'form': form})


def row_edit(request, pk):
    row = get_object_or_404(Row, pk=pk)
    if request.method == "POST":
        form = RowForm(request.POST, instance=row)
        if form.is_valid():
            row = form.save(commit=False)
            row.author = request.user
            row.published_date = timezone.now()
            row.save()
            return redirect('row_detail', pk=row.pk)
    else:
        form = RowForm(instance=row)
    return render(request, 'kartoteka/row_edit.html', {'form': form})


def row_delete(request, pk):
    #row = get_object_or_404(Row, pk=pk)
    row = Row.objects.get(pk=pk)
    row.delete()
    return redirect('row_list')


def row_search(request):
    form = SearchForm()
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data

            if cd['col'] == 'investor':
                results = Row.objects.filter(investor__icontains=cd['query'])

            elif cd['col'] == 'contract_number':
                results = Row.objects.filter(contract_inumber__contains=cd['query'])

            elif cd['col'] == 'zip_code':
                results = Row.objects.filter(zip_code__icontains=cd['query'])

            elif cd['col'] == 'manager':
                results = Row.objects.filter(manager__icontains=cd['query'])

            elif cd['col'] == 'design':
                results = Row.objects.filter(design__icontains=cd['query'])

            elif cd['col'] == 'implementation_date':
                results = Row.objects.filter(implementation_date__icontains=cd['query'])

            elif cd['col'] == 'coutry':
                results = Row.objects.filter(coutry__icontains=cd['query'])

            # Obliczenie całkowitej liczby wyników.
            total_results = results.count()
            return render(request,
                          'kartoteka/search.html',
                          {'form': form,
                           'cd': cd,
                           'results': results,
                           'total_results': total_results})
    else:
        return render(request,
                      'kartoteka/search.html',
                      {'form': form},)
