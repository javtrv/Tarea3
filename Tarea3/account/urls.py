'''
	@Authors
	Mariagabriela Jaimes (14-10526)
	Javier Medina (12-10400)
'''
from django.conf.urls import url, include
from django.contrib import admin
from . views import home, registro,loginUsuario

urlpatterns = [
    url(r'^$', home),
    url(r'^registro/', registro),
    url(r'^login/$',  loginUsuario ),
    url(r'^inicio/', {'template_name':'account/inicio.html'} )
]