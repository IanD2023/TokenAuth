from usuarios.models import validacao_email
from datetime import date,timedelta,datetime

class tokendeAutenticacao:


    def __init__(self,codigo,data):
        
        self.codigo=codigo
        self.data=data
        
    def token(self):

        try:

            token=validacao_email.objects.get(codigo=self.codigo)

            return token
        
        except:

            return False

    def criarToken(self,tokendevalidacao):

        try:

            validacao_email.objects.create(codigo=self.codigo,token_validacao=tokendevalidacao,data=self.data,validade_token=1)
            
            return True
        
        except:

            return False


    def contabilizaValidadeToken(self):
         
        try:
             
            token=validacao_email.objects.get(codigo=self.codigo)

            if str(token.data) != self.data.strftime("%Y-%m-%d"):
                
                token.data = self.data
                token.validade_token = int(token.validade_token) + 1
                token.save()

                return True

        except:

            return False        


    def atualizaToken(self,tokendevalidacao):

        try:

            token=validacao_email.objects.get(codigo=self.codigo)

            token.token_validacao=tokendevalidacao
            token.data=self.data
            token.validade_token=1
            token.save()

        except:

            return False
        

    def criaNovoToken(self,novotoken):
         
         try:
         
            token=validacao_email.objects.get(codigo=self.codigo)
            aviso_validade_token = 5

            if int(token.validade_token) == aviso_validade_token and token.data_ultimo_token != self.data.strftime("%Y-%m-%d"):

                token.proximo_token = novotoken
                token.data_ultimo_token = self.data
                token.save() 

         except:           
               
               return False

    def fimValidadeToken(self):

        try:

            fimvalidadetoken=validacao_email.objects.get(codigo=self.codigo)

            validadeToken = 5
            
            if int(fimvalidadetoken.validade_token) == validadeToken and str(fimvalidadetoken.data) != self.data.strftime("%Y-%m-%d"):
                            
                fimvalidadetoken.token_validacao = fimvalidadetoken.proximo_token
                fimvalidadetoken.validade_token = 0
                fimvalidadetoken.save()

                return True
            
            else:

                return False
            
        except:

            return False


                
