from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Property
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

class PropertyListView(ListView):
    model = Property
    template_name = 'listings/property_list.html'
    context_object_name = 'properties'

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'listings/property_detail.html'

class PropertyCreateView(LoginRequiredMixin, CreateView):
    model = Property
    fields = ['title', 'description', 'price', 'area_sqft', 'location', 'property_type']
    template_name = 'listings/property_form.html'

    def form_valid(self, form):
        form.instance.listed_by = self.request.user
        return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Property
    fields = ['title', 'description', 'price', 'area_sqft', 'location', 'property_type']
    template_name = 'listings/property_form.html'

    def form_valid(self, form):
        form.instance.listed_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        return self.request.user == property.listed_by

class PropertyDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Property
    success_url = reverse_lazy('property-list')
    template_name = 'listings/property_confirm_delete.html'

    def test_func(self):
        property = self.get_object()
        return self.request.user == property.listed_by

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'listings/register.html', {'form': form})