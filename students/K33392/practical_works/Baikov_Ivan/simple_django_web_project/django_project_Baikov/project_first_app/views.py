from django.shortcuts import render, get_object_or_404, redirect
from .models import CarOwner
from django.views import View
from .models import Car
from .forms import CarOwnerForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CarForm
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login

def list_owners(request):
    owners = CarOwner.objects.all()
    return render(request, 'owners_list.html', {'owners': owners})

class CarList(View):
    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'cars_list.html', {'cars': cars})

class CarDetail(View):
    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        return render(request, 'car_detail.html', {'car': car})
    
def add_owner(request):
    if request.method == 'POST':
        form = CarOwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owners_list') 
    else:
        form = CarOwnerForm()

    return render(request, 'add_owner.html', {'form': form})

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('cars_list')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_form.html'
    success_url = reverse_lazy('cars_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('cars_list')

def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('login')
    else:
        user_form = UserCreationForm()
        profile_form = UserProfileForm()
    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})
