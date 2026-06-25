from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Farmer
from .forms import FarmerForm

class FarmerListView(LoginRequiredMixin, ListView):
    model = Farmer
    template_name = 'farmers/farmer_list.html'
    context_object_name = 'farmers'

class FarmerDetailView(LoginRequiredMixin, DetailView):
    model = Farmer
    template_name = 'farmers/farmer_detail.html'
    context_object_name = 'farmer'

class FarmerCreateView(LoginRequiredMixin, CreateView):
    model = Farmer
    form_class = FarmerForm
    template_name = 'farmers/farmer_form.html'
    success_url = reverse_lazy('farmer_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FarmerUpdateView(LoginRequiredMixin, UpdateView):
    model = Farmer
    form_class = FarmerForm
    template_name = 'farmers/farmer_form.html'
    success_url = reverse_lazy('farmer_list')

class FarmerDeleteView(LoginRequiredMixin, DeleteView):
    model = Farmer
    template_name = 'farmers/farmer_confirm_delete.html'
    success_url = reverse_lazy('farmer_list')
