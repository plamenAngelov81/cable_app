from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from cable_app.cable.forms import CableCreateForm
from cable_app.cable.models import Cable


def index(request):
    cables = Cable.objects.all()
    context = {
        'cables': cables
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
