from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import UsuarioFrom
from braces.views import GroupRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Perfil
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, User

# Create your views here.
class ContaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    template_name = "criar_conta.html"
    form_class = UsuarioFrom
    success_url = reverse_lazy("login")
    login_url = reverse_lazy("login")
    group_required = u"admin"

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name = "funcionario") 

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url 
    
    #PERFIL

class PerfilUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = "../templates/cadastrar.html"
    model = Perfil
    fields = ["nome", "bi", "contato1", "contato2", "imagem"]
    success_url = reverse_lazy("perfil")
    login_url = "login.html"
    group_required = u"funcionario"

    def get_object(self, queryset = None):
        self.object = get_object_or_404(Perfil, usuario = self.request.user)
        self.object = get_object_or_404 (Perfil, pk = self.kwargs['pk'], usuario = self.request.user) 
        return self.object
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Editar Perfil"
        return context

class PerfilList1(GroupRequiredMixin, LoginRequiredMixin, ListView):
    template_name = "perfil.html"
    model = Perfil
    fields = ["usuario", "nome", "bi", "contato1", "contato2"]
    login_url = "login.html"
    group_required = u"funcionario"

    def get_queryset(self):
        self.object_list=Perfil.objects.filter(usuario= self.request.user)
        return self.object_list
    
    def get_object(self, queryset = None):
        self.object = get_object_or_404(Perfil, usuario = self.request.user)
        self.object = get_object_or_404 (Perfil, pk = self.kwargs['pk'], usuario = self.request.user) 
        return self.object

class PerfilList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Perfil
    fields = ["nome", "bi", "contato1", "contato2", "imagem"]
    template_name = "listarPerfil.html"
    login_url = reverse_lazy("login")
    group_required = u"admin"
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Lista de Perfís"
        return context

class PerfilDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Perfil
    template_name = "cadastros/templates/excluir.html"
    success_url = reverse_lazy("login")
    login_url = reverse_lazy("login")
    group_required = u"admin"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Perfil"
        return context

