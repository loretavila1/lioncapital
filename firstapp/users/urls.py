from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.register, name="register"),
    path("login/",views.login_view, name="login"),
    path('profile/', views.profile, name='profile'),
    path("logout/",views.logout_view, name="logout"),
    path("index", views.index, name="index"),
    path('desarrollos/', views.desarrollos, name='desarrollos'),
    path('capacitacion/', views.capacitacion, name='capacitacion'),
    path('manada/', views.manada, name='manada'),
    path('sucursales/', views.sucursales, name='sucursales'),
    path('desarrollos/luhm', views.lhm, name='luhm'),
    path('desarrollos/malik', views.mlk, name='malik'),
    path('desarrollos/monaco', views.mnc, name='monaco'),
    path('desarrollos/marieta', views.mrt, name='marieta'),
    path('desarrollos/granplaya', views.gpl, name='granplaya'),
    path('desarrollos/velastelchac', views.vlt, name='velas'),
    path('desarrollos/playagaviotas', views.plg, name='gaviotas'),
    path('desarrollos/cocoteros', views.cct, name='cocoteros'),
    path('desarrollos/umanindustrial', views.uman, name='uman'),
    path('desarrollos/conkal', views.cnkl, name='conkal'),
    path('desarrollos/caminoreal', views.cmnrl, name='caminoreal'),
    path('desarrollos/haciendascelestun', views.clstn, name='celestun'),
    path('profile/logros/', views.logro, name='logros'),
    path('profile/progreso/', views.progreso, name='progreso'),
    path('profile/progreso/experto', views.exp, name='experto'),
    path('profile/progreso/asesorando', views.ase, name='asesorando'),
    path('profile/progreso/liderando', views.lid, name='liderando'),
    path('profile/progreso/leontribu', views.tribu, name='tribu'),
    path('profile/account', views.cuenta, name='cuenta'),
    path('capacitacion/administracion', views.adm, name='administracion'),
    path('capacitacion/crm', views.crm, name='crm'),
    path('capacitacion/politicas', views.pol, name='politicas'),
    path('capacitacion/videoconferencias', views.video, name='videoconferencias'),

]
