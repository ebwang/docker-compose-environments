from django.contrib import admin
from .models import Pessoas

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome', 'email')
    #Tem que ser uma tupla ou lista por isso a virgula
    search_fields = ('nome',)


# Register your models here.
admin.site.register(Pessoas,ListandoPessoas)