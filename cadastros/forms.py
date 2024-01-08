from django import forms
from .models import Certificado, Declaracao, Historico
from .models import Levantamento_Certificado, Levantamento_Declaracao, Levantamento_Historico

class CertificadoForm(forms.ModelForm):

    class Meta:
        model = Levantamento_Certificado
        field = "__all__"
        exclude = ("data", "documento", "funcionario")

class DeclaracaoForm(forms.ModelForm):

    class Meta:
        model = Levantamento_Declaracao
        field = "__all__"
        exclude = ("data", "documento", "funcionario")

class HistoricoForm(forms.ModelForm):

    class Meta:
        model = Levantamento_Historico
        field = "__all__"
        exclude = ("data", "documento", "funcionario")