from django.urls import path
from django.conf import settings
from django.template.response import TemplateResponse 
from .views import home, autenticar,cadastrar,senha,registraacesso,alterarsenha,layout


urlpatterns = [

    path('', home,name="home"),
    ##path('home/', layout,name="layout"),
    path('autenticar/', autenticar,name="autenticar"),
    path('cadastrar/', cadastrar,name="criaracesso"),
    path('senha/', senha,name="senha"),
    path('acess/', registraacesso,name="registraacesso"),
    path('usr/', alterarsenha,name="alterarsenha")
]

