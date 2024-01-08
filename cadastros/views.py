from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import Certificado, Declaracao, Peticao, Historico,Levantamento_Certificado, Levantamento_Declaracao, Levantamento_Historico
from .forms import CertificadoForm, DeclaracaoForm, HistoricoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group, User
import pandas as pd
import sqlite3

# Create your views here.

#relatórios
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from django.template.loader import render_to_string, get_template
from xhtml2pdf import pisa

            #Certiificadoe
    model = Declaracao
    fields = ["nome_utente", "bi", "quantidade", "nota"]
    template_name = "cadastrar.html"
    success_url = reverse_lazy("listar-declaracao")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def form_valid(self, form):
        #Antes do Super o objecto não está criado nem salvou no banco
        form.instance.funcionario = self.request.user
        url=super().form_valid(form)
        #Depois do Super o objecto já foi criado
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Declaração"
        return context

class DeclaracaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Declaracao
    fields = ["__all__"]
    template_name = "listarDeclaracao.html"
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Lista de Declarações"
        return context
    
class DeclaracaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Declaracao
    fields = ["nome_utente", "bi", "quantidade", "nota", "estado"]
    template_name = "cadastrar.html"
    success_url = reverse_lazy("listar-declaracao")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Alterar Declaração"
        return context

class DeclaracaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Declaracao
    template_name = "excluir.html"
    success_url = reverse_lazy("listar-declaracao")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Declaração"
        return context
    
#Petição
class PeticaoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Peticao
    fields = ["numero_peticao", "nome_utente", "quantidade", "assunto", "nota"]
    template_name = "cadastrar.html"
    success_url = reverse_lazy("listar-peticao")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def form_valid(self, form):
        #Antes do Super o objecto não está criado nem salvou no banco
        form.instance.funcionario = self.request.user
        url=super().form_valid(form)
        #Depois do Super o objecto já foi criado
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Petição"
        return context

class PeticaoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Peticao
    fields = ["__all__"]
    template_name = "listarPeticao.html"
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Lista de Petições"
        return context
    
class PeticaoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Peticao
    fields = ["numero_peticao", "nome_utente", "quantidade", "assunto", "nota", "estado"]
    template_name = "cadastrar.html"
    success_url = reverse_lazy("listar-peticao")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Alterar Petição"
        return context

class PeticaoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Peticao
    template_name = "excluir.html"
    success_url = reverse_lazy("listar-peticao")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Petição"
        return context
    
    #Histórico
class HistoricoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Historico
    fields = ["nome_utente", "bi", "quantidade", "ano", "nota"]
    template_name = "cadastrar.html"
    success_url = reverse_lazy("listar-historico")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def form_valid(self, form):
        #Antes do Super o objecto não está criado nem salvou no banco
        form.instance.funcionario = self.request.user
        url=super().form_valid(form)
        #Depois do Super o objecto já foi criado
        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Cadastrar Histórico de Notas"
        return context

class HistoricoList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    model = Historico
    fields = ["__all__"]
    template_name = "listarHistorico.html"
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Lista de Históricos de Notas"
        return context
    
class HistoricoUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Historico
    fields = ["nome_utente", "bi", "quantidade", "ano", "nota", "estado"]
    template_name = "cadastrar.html"
    success_url = reverse_lazy("listar-historico")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Alterar Histórico de Notas"
        return context

class HistoricoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Historico
    template_name = "excluir.html"
    success_url = reverse_lazy("listar-historico")
    login_url = reverse_lazy("login")
    group_required = u"admin", u"funcionario"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["titulo"] = "Excluir Histórico de Notas"
        return context
    
#Relatórios
def ExcelCertificado(request):

    conn=sqlite3.connect('db.sqlite3')
    comando_sql = 'select * from cadastros_certificado'
    excel=pd.read_sql_query(comando_sql, conn)
    excel.to_excel("documentos/certificados.xlsx")
    excel.to_csv("documentos/certificados.csv")
   
    atividade = Certificado.objects.all()
   
    return render(request, 'index.html')

def ExcelDeclaracao(request):

    conn=sqlite3.connect('db.sqlite3')
    comando_sql = 'select * from cadastros_declaracao'
    excel=pd.read_sql_query(comando_sql, conn)
    excel.to_excel("documentos/declaracao.xlsx")
    excel.to_csv("documentos/declaracao.csv")
   
    atividade = Declaracao.objects.all()
   
    return render(request, 'index.html')

def ExcelPeticao(request):

    conn=sqlite3.connect('db.sqlite3')
    comando_sql = 'select * from cadastros_peticao'
    excel=pd.read_sql_query(comando_sql, conn)
    excel.to_excel("documentos/petição.xlsx")
    excel.to_csv("documentos/petição.csv")
   
    atividade = Peticao.objects.all()
   
    return render(request, 'index.html')

def ExcelHistorico(request):

    conn=sqlite3.connect('db.sqlite3')
    comando_sql = 'select * from cadastros_historico'
    excel=pd.read_sql_query(comando_sql, conn)
    excel.to_excel("documentos/historico_de_notas.xlsx")
    excel.to_csv("documentos/historico_de_notas.csv")
   
    atividade = Historico.objects.all()
   
    return render(request, 'index.html')


#LEVANTAMENTOS certificado
def LevantamentoCertificado(request, **kwargs):
    
    if request.method == "POST":
       form = CertificadoForm(request.POST)
       dados1 = Certificado.objects.filter(pk = kwargs["pk"])
       context = {
           "form":form
       }
       if form.is_valid:
           form.instance.funcionario = request.user
           form.instance.documento = kwargs["pk"]
           form.save()
           return render(request, "listarCertificado.html")
       else:
           pass
           return render(request, "index.html")
    
    elif request.method == "GET":
        dados = Levantamento_Certificado.objects.filter(documento = kwargs["pk"])
        form = CertificadoForm()
        
        context = {
            "dados":dados,
            "form":form,
        }
        return render(request, "LevantamentoCertificado.html", context)

    else:
        pass

    return render(request, "listarCertificado.html")


#LEVANTAMENTOS declaracao
def LevantamentoDeclaracao(request, **kwargs):
    
    if request.method == "POST":
       form1 = DeclaracaoForm(request.POST)
       dados1 = Declaracao.objects.filter(pk = kwargs["pk"])
       context = {
           "form":form1
       }
       if form1.is_valid:
           form1.instance.funcionario = request.user
           form1.instance.documento = kwargs["pk"]
           form1.save()
           return render(request, "listarDeclaracao.html")
       else:
           pass
           return render(request, "index.html")
    
    elif request.method == "GET":
        dados = Levantamento_Declaracao.objects.filter(documento = kwargs["pk"])
        form1 = DeclaracaoForm()
        
        context = {
            "dados":dados,
            "form":form1,
        }
        return render(request, "LevantamentoDeclaracao.html", context)

    else:
        pass

    return render(request, "listarDeclaracao.html")

#LEVANTAMENTO historico
def LevantamentoHistorico(request, **kwargs):
    
    if request.method == "POST":
       form2 = HistoricoForm(request.POST)
       dados1 = Historico.objects.filter(pk = kwargs["pk"])
       context = {
           "form":form2
       }
       if form2.is_valid:
           form2.instance.funcionario = request.user
           form2.instance.documento = kwargs["pk"]
           form2.save()
           return render(request, "listarHistorico.html")
       else:
           pass
           return render(request, "index.html")
    
    elif request.method == "GET":
        dados = Levantamento_Historico.objects.filter(documento = kwargs["pk"])
        form2 = HistoricoForm()
        
        context = {
            "dados":dados,
            "form":form2,
        }
        return render(request, "LevantamentoHistorico.html", context)

    else:
        pass

    return render(request, "listarHistorico.html")