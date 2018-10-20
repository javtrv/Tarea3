'''
	@Authors
	Mariagabriela Jaimes (14-10526)
	Javier Medina (12-10400)
'''


"""Tarea3 URL Configuration

"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$', auth_views.logout),
    url(r'^', include('account.urls'))
]
