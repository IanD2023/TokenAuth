from usuarios.models import funcionario,token_do_funcionario
from datetime import *
from tokenbag.settings import *


class Funcionario:


    def __init__(self,nome):

        self.nome=nome

    def funcionaro(self):

        try:

            funcionarioToken=funcionario.objects.get(nome=self.nome,ativo=True)
            return funcionarioToken
        
        except:

            return False

    def funcionarioID(self):

        id=self.funcionaro().id
        
        return id
    
    def ativo(self):

        status=funcionario.objects.get(nome=self.nome)

        return status.ativo
    
    def alteraCPF(self,cpf):

        try:

            funcionarioCPF=self.funcionaro()
            funcionarioCPF.cpf = (f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}")
            funcionarioCPF.save()

            return True
        
        except:    
            
            return False
        
    def tokensdoFuncionario(self):


        def formatadata(data):

            return data.strftime("%d-%m-%Y")

        hoje = datetime.now(IST)
        ontem = hoje - timedelta(1) 
        anteontem = ontem - timedelta(1)

        tokens=token_do_funcionario.objects.filter(
        funcionario_id=self.funcionarioID(),
        data_do_envio__gte=anteontem.strftime("%Y-%m-%d"),
        ##data_do_envio__time__lte="08:00:00",
        )

        tokensListar={}

        for x in tokens:

            dataenvio = formatadata(x.data_do_envio)
            
            if dataenvio == formatadata(hoje.today()):

                tokensListar['senhahoje']=x.valor

            if dataenvio == formatadata(hoje.today()-timedelta(1)):
                 
                 tokensListar['senhaontem']=x.valor

            if dataenvio == formatadata(hoje.today()-timedelta(2)):
                 
                 tokensListar['senhaanteontem']=x.valor
        
        return tokensListar



