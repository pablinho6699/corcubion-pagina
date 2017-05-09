from django.conf.urls import url
from pagina import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<equipo>\D+)/$', views.plantilla, name='plantilla'),
]