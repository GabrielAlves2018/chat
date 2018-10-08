
# -*- coding: utf-8 -*-

from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . import models
from .forms import UUIDUserForm, MensagemPV, UUIDUserFormEdit, Canal, Mensagem
from django.http import HttpResponseRedirect


class UserCreateView(CreateView):
    model = models.UUIDUser
    template_name = 'form.html'
    success_url = reverse_lazy('chat:home')
    form_class = UUIDUserForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.set_password(obj.password)
        obj.save()
        return super(UserCreateView, self).form_valid(form)

class Home(TemplateView):
    template_name = 'home.html'

class Chatpv(TemplateView):
    template_name = 'chatprivado.html'

class Mensagempv(CreateView):
    model = models.MensagemPV
    template_name = 'mensagempv.html'
    success_url = reverse_lazy('chat:home')
    form_class = MensagemPV
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sender = self.request.user
        obj.save()
        return super(Mensagempv, self).form_valid(form)

class Vermsnpv(ListView):
    model = models.MensagemPV
    template_name = 'vermsnpv.html'

class Verhistorico(ListView):
    model = models.MensagemPV
    template_name = 'verhistorico.html'

class Msnedit(UpdateView):
    model = models.MensagemPV
    template_name = 'msnedit.html'
    success_url= reverse_lazy('chat:home')
    form_class = MensagemPV

class Msndelete(DeleteView):
    model = models.MensagemPV
    template_name = 'msndelete.html'
    success_url= reverse_lazy('chat:home')
    form_class = MensagemPV

class Perfil(ListView):
    model = models.UUIDUser
    template_name = 'perfildados.html'

class Perfiledit(UpdateView):
    model = models.UUIDUser
    template_name = 'perfiledit.html'
    success_url = reverse_lazy('chat:login')
    form_class = UUIDUserFormEdit

class Perfildelete(DeleteView):
    model = models.UUIDUser
    template_name = 'perfildelete.html'
    success_url = reverse_lazy('chat:home')
    form_class = UUIDUserForm

class ListaCanais(ListView):
    model = models.Canal
    template_name = 'listacanais.html'

class CanalDetail(DetailView):
    model = models.Canal
    template_name = 'canaldetail.html'
    def get_context_data(self, **kwargs):
        kwargs['mensagens'] = models.Mensagem.objects.all()
        return super(CanalDetail, self).get_context_data(**kwargs)

class CanalCreate(CreateView):
    model = models.Canal
    template_name = 'canalcreate.html'
    success_url = reverse_lazy('chat:home')
    form_class = Canal
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CanalCreate, self).form_valid(form)

class MyChannels(ListView):
    model = models.Canal
    template_name = 'mychannels.html'


class EditChannel(UpdateView):
    model = models.Canal
    template_name = 'editchannel.html'
    success_url = reverse_lazy('chat:home')
    form_class = Canal

class RemoveChannel(DeleteView):
    model = models.Canal
    template_name = 'channeldelete.html'
    success_url = reverse_lazy('chat:home')
    form_class = Canal

class MensagemCanal(CreateView):
    model = models.Mensagem
    template_name = 'mensagemcanal.html'
    success_url = reverse_lazy('chat:home')
    form_class = Mensagem
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(MensagemCanal, self).form_valid(form)

