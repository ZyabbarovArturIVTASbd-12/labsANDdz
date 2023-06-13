from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return HttpResponse("<h1>О себе</h1>")


def table_view(request, tk):
    table = []
    model = [CarType, Car, TravelPoint, OwnerTravelPoint, CarPass, DataOfPassingCar]
    title = model[tk].title

    for x in model[tk].objects.all():
        table.append(x.get_dict())

    return render(request, 'main/table_show.html', {'table': table, 'names': model[tk].names, 'title': title, 'table_id': tk})


def table_change(request, tk, el, command):
    el -= 1
    forms = [CarTypeForm, CarForm, TravelPointForm, OwnerTravelPointForm, CarPassForm, DataOfPassingCarForm]
    model = [CarType, Car, TravelPoint, OwnerTravelPoint, CarPass, DataOfPassingCar]
    form = forms[tk]

    error = ''

    if command == 'edit':
        form = forms[tk].clone_instance(model[tk].objects.all()[el])

        if request.method == 'POST':
            form = forms[tk].clone(request.POST)
            if form.is_valid():
                edit_model = model[tk].objects.all()[el]
                for name in form.Meta.fields:
                     setattr(edit_model, name, form.cleaned_data.get(name))
                edit_model.save()
                return redirect('table_show', tk)
            else:
                error = 'Данные введены некорректно.'


    if command == 'add':
        if request.method == 'POST':
            form = forms[tk].clone(request.POST)
            if form.is_valid():
                form.save()
                return redirect('table_show', tk)
            else:
                error = 'Данные введены некорректно.'

    if command == 'delete':
        model[tk].objects.all()[el].delete()
        return redirect('table_show', tk)

    return render(request, 'main/form.html', {'form': form, 'names': model[tk].names, 'error': error})
