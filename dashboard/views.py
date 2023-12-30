from django.shortcuts import render
from django.http import HttpResponse
from dashboard.forms import CityForm
from .models import CityModel
from .helper import get_weather_data


def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            city_name = form.cleaned_data['city_name']
            weather_data = get_weather_data(city_name)

    elif request.method == 'GET':
        city_name = CityModel.objects.latest('date_added').city_name
        weather_data = get_weather_data(city_name)

    template_name = 'home.html'
    context = {'form': form, 'weather_data': weather_data}
    print(context)
    return render(request, template_name, context)


def history(request):
    template_name = 'history.html'
    cities = CityModel.objects.all().order_by('-date_added')[:5]
    weather_data_list = []
    for city in cities:
        weather_data_list.append(get_weather_data(city.city_name))
    context = {
        'weather_data_list': weather_data_list
    }
    return render(request, template_name, context)
