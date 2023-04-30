from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from cable_app.cable import forms
from cable_app.cable.forms import CableCreateForm, OrderCable, EditOrderForm
from cable_app.cable.models import Cable, Order


@login_required(login_url='account login')
def index(request):
    cables = Cable.objects.all()
    orders = Order.objects.all()
    if request.method == "GET":
        form = forms.CableCreateForm()
    else:
        form = forms.CableCreateForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'cables': cables,
        'form': form,
        'orders': orders
    }
    return render(request, 'cables/index.html', context)


class CableCreate(generic.CreateView):
    model = Cable
    template_name = 'cables/cable_create.html'
    form_class = CableCreateForm
    success_url = reverse_lazy('index')


class CableDetailsView(generic.DetailView):
    template_name = 'cables/cable_details.html'
    model = Cable


class CableEditView(generic.UpdateView):
    model = Cable
    template_name = 'cables/cable_edit.html'
    form_class = CableCreateForm
    success_url = reverse_lazy('index')


class CableDeleteView(generic.DeleteView):
    model = Cable
    template_name = 'cables/cable_delete.html'
    success_url = reverse_lazy('index')


def order_cable(request, pk):
    cable = Cable.objects.filter(pk=pk).get
    if request.method == 'POST':
        form = OrderCable(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = OrderCable()
    context = {
        'form': form,
        'cable': cable
    }
    return render(request, 'orders/order_cable.html', context)


class EditOrderView(generic.UpdateView):
    template_name = 'orders/order_edit.html'
    model = Order
    form_class = EditOrderForm
    success_url = reverse_lazy('index')
