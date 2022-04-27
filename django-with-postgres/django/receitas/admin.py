from django.contrib import admin
from .models import Receitas


class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_receita')
    #Tem que ser uma tupla ou lista por isso a virgula
    search_fields = ('nome_receita',)
    #Tem que ser uma tupla ou lista por isso a virgula
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10


# Register your models here.
admin.site.register(Receitas,ListandoReceitas)