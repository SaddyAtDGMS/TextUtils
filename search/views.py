from django.shortcuts import render
from django.views import View
from .forms import SearchForm
from common.models import Minemast


# Create your views here.
# newapp/views.py


def search_view_minecode(request):
    form = SearchForm()
    results = []

    if request.method == 'GET' and 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # results = Minemast.objects.filter(name__icontains=query)
            results = Minemast.objects.filter(mine__icontains=query)

    return render(request, 'search_minecode.html', {'form': form, 'results': results})
