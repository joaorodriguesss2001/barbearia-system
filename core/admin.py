from django.contrib import admin

from .models import Barbeiro, Cliente, Agendamento


admin.site.register(Barbeiro)
admin.site.register(Cliente)
admin.site.register(Agendamento)