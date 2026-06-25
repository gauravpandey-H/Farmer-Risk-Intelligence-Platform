from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Crop
from .forms import CropForm

class CropListView(LoginRequiredMixin, ListView):
    model = Crop
    template_name = 'crops/crop_list.html'
    context_object_name = 'crops'

    def get_queryset(self):
        if hasattr(self.request.user, 'farmer'):
            return Crop.objects.filter(farmer=self.request.user.farmer)
        return Crop.objects.none()

class CropDetailView(LoginRequiredMixin, DetailView):
    model = Crop
    template_name = 'crops/crop_detail.html'
    context_object_name = 'crop'

class CropCreateView(LoginRequiredMixin, CreateView):
    model = Crop
    form_class = CropForm
    template_name = 'crops/crop_form.html'
    success_url = reverse_lazy('crop_list')

    def get_initial(self):
        initial = super().get_initial()
        if hasattr(self.request.user, 'farmer'):
            initial['farmer'] = self.request.user.farmer
        return initial

class CropUpdateView(LoginRequiredMixin, UpdateView):
    model = Crop
    form_class = CropForm
    template_name = 'crops/crop_form.html'
    success_url = reverse_lazy('crop_list')

class CropDeleteView(LoginRequiredMixin, DeleteView):
    model = Crop
    template_name = 'crops/crop_confirm_delete.html'
    success_url = reverse_lazy('crop_list')
