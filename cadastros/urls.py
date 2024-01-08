from django.urls import path
from .views import DeclaracaoCreate, DeclaracaoList, DeclaracaoUpdate, DeclaracaoDelete
from .views import CertificadoCreate, CertificadoList, CertificadoUpdate, CertificadoDelete
from .views import PeticaoCreate, PeticaoList, PeticaoUpdate, PeticaoDelete
from .views import HistoricoCreate, HistoricoList, HistoricoUpdate, HistoricoDelete
from .views import ExcelHistorico, ExcelCertificado, ExcelDeclaracao, ExcelPeticao
from .views import LevantamentoCertificado, LevantamentoDeclaracao, LevantamentoHistorico

urlpatterns = [
    path("certificado/cadastrar/", CertificadoCreate.as_view(), name="cadastrar-certificado"),
    path("certificado/listar/", CertificadoList.as_view(), name="listar-certificado"),
    path("certificado/editar/<int:pk>/", CertificadoUpdate.as_view(), name="editar-certificado"),
    path("certificado/deletar/<int:pk>/", CertificadoDelete.as_view(), name="deletar-certificado"),

    path("declaracao/cadastrar/", DeclaracaoCreate.as_view(), name="cadastrar-declaracao"),
    path("declaracao/listar/", DeclaracaoList.as_view(), name="listar-declaracao"),
    path("declaracao/editar/<int:pk>/", DeclaracaoUpdate.as_view(), name="editar-declaracao"),
    path("declaracao/deletar/<int:pk>/", DeclaracaoDelete.as_view(), name="deletar-declaracao"),

    path("peticao/cadastrar/", PeticaoCreate.as_view(), name="cadastrar-peticao"),
    path("peticao/listar/", PeticaoList.as_view(), name="listar-peticao"),
    path("peticao/editar/<int:pk>/", PeticaoUpdate.as_view(), name="editar-peticao"),
    path("peticao/deletar/<int:pk>/", PeticaoDelete.as_view(), name="deletar-peticao"),

    path("historico/cadastrar/", HistoricoCreate.as_view(), name="cadastrar-historico"),
    path("historico/listar/", HistoricoList.as_view(), name="listar-historico"),
    path("historico/editar/<int:pk>/", HistoricoUpdate.as_view(), name="editar-historico"),
    path("historico/deletar/<int:pk>/", HistoricoDelete.as_view(), name="deletar-historico"),


    path("levantamento/certificado/<int:pk>/", LevantamentoCertificado, name="levantamento-certificado"),
    path("levantamento/declaracao/<int:pk>/", LevantamentoDeclaracao, name="levantamento-declaracao"),
    path("levantamento/historico/<int:pk>/", LevantamentoHistorico, name="levantamento-historico"),
    #path("historico/deletar/<pk>:int", HistoricoDelete.as_view(), name="deletar-historico"),
    
      #Relatório
    path("historico-de-notas", ExcelHistorico, name="historico"),
    path("certificado", ExcelCertificado, name="certificado"),
    path("declaracao", ExcelDeclaracao, name="declaracao"),
    path("peticao", ExcelPeticao, name="peticao"),
]