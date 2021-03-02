from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from main.models import Item
from main.forms import CreateItemForm


class HomeView(generic.CreateView):
    model = Item
    template_name = 'main/index.html'
    success_url = reverse_lazy('main:home')
    form_class = CreateItemForm
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context

