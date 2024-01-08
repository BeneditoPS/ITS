from django.shortcuts import render
from cadastros.models import Certificado, Declaracao, Historico

# Create your views here.

def Index(request):
    dados = Certificado.objects.all()
    buscaC = Certificado.objects.filter(estado='Busca')
    buscaD = Declaracao.objects.filter(estado='Busca')
    buscaH = Historico.objects.filter(estado='Busca')
    busca = buscaC.count()+buscaD.count()+buscaH.count()
    
    digitalizadoC = Certificado.objects.filter(estado='Digitalizado')
    digitalizadoD = Declaracao.objects.filter(estado='Digitalizado')
    digitalizadoH = Historico.objects.filter(estado='Digitalizado')
    digitalizado = digitalizadoC.count()+digitalizadoD.count()+digitalizadoH.count()
    
    concluidoC = Certificado.objects.filter(estado='Concluido')
    concluidoD = Declaracao.objects.filter(estado='Concluido')
    concluidoH = Historico.objects.filter(estado='Concluido')
    concluido = concluidoC.count()+concluidoD.count()+concluidoH.count()
        
    return render(request, "index.html", {'busca': busca, 'digitalizado':digitalizado, 'concluido':concluido})
