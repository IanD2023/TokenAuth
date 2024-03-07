from django.contrib.auth.models import User
from services import MD5


class usuarioTokenAuth:


     def __init__(self,nome,codigo):
          
          self.nome = nome
          self.codigo = codigo

     def usuario(self):

        try:

            usuarioToken=User.objects.get(username=self.codigo)
     
            return usuarioToken
        
        except:

            return False  
        
     def cpf(self,cpf):
         
         try:

             cpfdoUsuario=User.objects.get(username=self.codigo,cpf=cpf)

             return  cpfdoUsuario.cpf

         except:
             
             return False
     
     def criarUsuario(self,cpf,senha,palavra_secreta,hash_usuario):

        try:

            user = User.objects.create_user(
                                username=self.codigo,first_name=self.nome, cpf=cpf,password=senha,pin=palavra_secreta,is_staff=False,is_superuser=False,hash_usuario=MD5.converter(hash_usuario))
            user.save()

            return True

        except:

            return False
        
     def alterarSenha(self,novasenha):

        usuario=self.usuario()
        usuario.set_password(novasenha)
        usuario.save()  


     def pinUsuario(self,pin):
         
         try:

            pinUsuario= User.objects.get(username=self.codigo,pin=pin)

            return pinUsuario
         
         except:
             
             return False
     