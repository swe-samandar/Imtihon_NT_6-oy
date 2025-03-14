from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import House
from .forms import HouseForm


class Home(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        city = request.GET.get('city_')
        district = request.GET.get('district_')
        price = request.GET.get('price_')
        rooms = request.GET.get('rooms_')
        floor = request.GET.get('floor_')

        # Filtrlash shartlari
        houses = House.objects.all()
        if city:
            houses = houses.filter(city__icontains=city)
        if district:
            houses = houses.filter(district__icontains=district)
        if price:
            houses = houses.filter(price__lte=price)
        if rooms:
            houses = houses.filter(rooms=rooms)
        if floor:
            houses = houses.filter(floor=floor)

        paginator = Paginator(houses, 1) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'house/home.html', {'page_obj': page_obj})



class HouseDetail(View):
    def get(self, request, pk):
        house = get_object_or_404(House, id=pk)
        return render(request, 'house/detail.html', {'house': house})
    

class HouseCreate(View):
    def get(self, request):
        form = HouseForm()
        return render(request, 'house/create.html', {'form': form})
    

    def post(self, request):
        if request.method == 'POST':
            form = HouseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = HouseForm()
        return render(request, 'house/create.html', {'form': form})
    
class HouseUpdate(View):
    def get(self, request, pk):
        house = get_object_or_404(House, id=pk)
        form = HouseForm(instance=house)
        return render(request, 'house/update.html', {'form': form})
    
    def post(self, request, pk):
        house = get_object_or_404(House, id=pk)
        if request.method == 'POST':
            form = HouseForm(request.POST, request.FILES, instance=house)
            if form.is_valid():
                form.save()
                return redirect('house-detail', pk=pk)
        else:
            form = HouseForm(instance=house)
        return render(request, 'house/update.html', {'form': form}, pk=pk)
    
class HouseDelete(View):
    def get(self, request, pk):
        house = get_object_or_404(House, id=pk)
        return render(request, 'house/delete.html', {'house': house})


    def post(self, request, pk):
        house = get_object_or_404(House, id=pk)
        if request.method == 'POST':
            house.delete()
            return redirect('home')
        return render(request, 'house/delete.html', {'house': house})
        

class About(View):
    def get(self, request):
        return render(request, 'house/about.html')
    

class Contact(View):
    def get(self, request):
        return render(request, 'house/contact.html')
    

class Index(View):
    def get(self, request):
        return render(request, 'house/index.html')