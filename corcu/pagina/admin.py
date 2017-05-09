from django.contrib import admin

# Register your models here.from django.contrib import admin
from pagina.models import Equipos, Jugadores, Noticias, Patrocinadores

admin.site.register(Equipos)
admin.site.register(Jugadores)
admin.site.register(Noticias)
admin.site.register(Patrocinadores)