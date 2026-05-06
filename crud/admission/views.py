from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Admission
from .forms import AdmissionForm

# Create your views here.

class AdmissionListView(ListView):
    model = Admission
    template_name = 'admission/list.html'
    context_object_name = 'admission'

class AdmissionCreateView(CreateView):
    model = Admission
    form_class = AdmissionForm
    template_name = 'admission/form.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        messages.success(self.request, "Admission Created")
        return super().form_valid(form)
    

class AdmissionUpdateView(UpdateView):
    model = Admission
    form_class = AdmissionForm
    template_name = 'admission/form.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        messages.success(self.request, "Updated Successfully")
        return super().form_valid(form)
    
class AdmissionDeleteView(DeleteView):
    model = Admission
    template_name = 'admission/delete.html'
    success_url = reverse_lazy('list')
    
