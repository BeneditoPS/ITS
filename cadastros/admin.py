from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Peticao)
admin.site.register(Certificado)
admin.site.register(Declaracao)
admin.site.register(Historico)
admin.site.register(Levantamento_Certificado)
admin.site.register(Levantamento_Declaracao)
admin.site.register(Levantamento_Historico)