from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)
from django.contrib.auth.models import User
import re
from django.db import models
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

class Identificacao(models.Model):
     
     codigo = models.CharField(max_length=100,unique=True)
     id_cookie = models.CharField(max_length=100,null=True,unique=True)
     ativo = models.BooleanField(max_length=100)
     data_atualizacao = models.CharField(max_length=30,unique=True)

     class Meta:
        
        db_table = ''

     def __str__(self):

          self.codigo
          self.id_cookie
          self.ativo
          self.data_atualizacao

          return self


class funcionario(models.Model):

      id=models.UUIDField(primary_key=True,null=False)
      cpf = models.CharField(max_length=100,null=False)
      nome = models.CharField(max_length=100,null=False)
      codigo = models.CharField(max_length=30,null=False)
      data_de_criacao = models.DateTimeField(max_length=30,null=False)
      data_de_atualizacao = models.DateTimeField(max_length=30,null=True)
      ativo = models.BooleanField(null=False)
      tipo_de_funcionario = models.CharField(max_length=30,null=False)
      utiliza_token= models.BooleanField(null=False)
      numero_de_celular = models.CharField(max_length=30,null=True)
      recebe_sms_automatico = models.BooleanField(null=False)

      class Meta:
        
        db_table = "funcionario"

      def __str__(self):

          self.id
          self.cpf
          self.nome
          self.codigo
          self.data_de_criacao
          self.data_de_atualizacao
          self.ativo
          self.tipo_de_funcionario
          self.utiliza_token
          self.numero_de_celular
          self.recebe_sms_automatico
          
          return self
      

class token_do_funcionario(models.Model):
      
      id=models.UUIDField(primary_key=True,null=False)
      funcionario_id = models.UUIDField(null=False)
      data_do_envio = models.DateTimeField (max_length=30,null=False)
      valor = models.CharField(max_length=30,null=False)
      ip_remoto = models.CharField(max_length=30,null=False)

      class Meta:
        
        db_table = "token_do_funcionario"
        

      def __str__(self):

          self.id
          self.funcionario_id
          self.data_do_envio
          self.valor
          self.ip_remoto
          
          return self


class validacao_email(models.Model):
     
     codigo = models.CharField(max_length=100,unique=True)
     token_validacao = models.CharField(max_length=100,null=True)
     proximo_token = models.CharField(max_length=100,null=True)
     data_ultimo_token = models.CharField(max_length=30)
     validade_token = models.CharField(max_length=30)
     data = models.CharField(max_length=30,unique=True)

     class Meta:
        
        db_table = 'validacao_email'

     def __str__(self):

          self.codigo
          self.token_validacao
          self.proximo_token
          self.data_ultimo_token
          self.validade_token
          self.data

          return self      






