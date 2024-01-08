from django.urls import path
from .views import PerfilList, PerfilUpdate, ContaCreate, PerfilList1, PerfilDelete

urlpatterns = [
    path("criar-conta/", ContaCreate.as_view(), name="criar-conta"),
   

    #PERFIL
    path("perfil/", PerfilList1.as_view(), name="perfil"),
    path("perfil/listar/", PerfilList.as_view(), name="listar-perfis"),
    path("perfil/alterar/<int:pk>", PerfilUpdate.as_view(), name="alterar-perfil"),
    path("perfil/excluir/<int:pk>", PerfilDelete.as_view(), name="excluir-perfil"),
]