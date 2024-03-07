from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from datetime import date,timedelta,datetime
from .controller.funcionarioTokenBag import *
from .controller.usuarioTokenAuth import *
from .controller.funcionarioPDV import *
from .controller.validacaodeToken import *
from services import MD5
from services.email import enviar_email
from services import *
from tokenbag.settings import *
from services import codBarras
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
#hoje = datetime.now(IST).date()

def layout(request):

    return render(request, 'home/index.html')

def home(request):
    
    logout(request)

    return render(request, 'home/login.html')

def autenticar(request):

    Codigo=request.POST.get("codigo")
    Senha=request.POST.get("senha")
    validacaoemail=request.POST.get("validacaoemail")
    hash=request.POST.get("hash")
    cookieusuario=request.COOKIES.get('usr')
    hoje = datetime.now(IST).date()
    tokendevalidacao=MD5.gerarhash()
    validade_token=hoje + timedelta(4)
    
    if Codigo:
         
        UserMD5=MD5.converter(Codigo)

        if cookieusuario is True and cookieusuario != UserMD5:
                
            return render(request, 'home/login.html',{'cad':"negado"})
        
        user = authenticate(request,username=Codigo, password=Senha)
    
        if user:

            funcionariopdv=funcionarioPDV(Codigo)

            usuarioTokenauth=usuarioTokenAuth(funcionariopdv.nome(),Codigo)
            
            tokendeautenticacao=tokendeAutenticacao(Codigo,hoje)

            if hash:

                ##Utiliza o pin para realizar o login

                if validacaoemail == '1':

                    if usuarioTokenauth.usuario().pin == hash:

                        login(request, user)

                        return redirect(registraacesso)

                    else:  
                    
                     return render(request, 'home/login.html',{'cad':"solicitacodigo",'hash':'solicitacodigo',
                                                        'user':Codigo,'senha':Senha,'valor':'erro','codigo_acesso':'1'}) 
                ## Utiliza o token temporario para realizar o login          
                else:

                    if tokendeautenticacao.token().token_validacao == hash:

                        login(request, user)

                        return redirect(registraacesso)

                    else:  
                        
                        return render(request, 'home/login.html',{'cad':"solicitacodigo",'hash':'solicitacodigo',
                                                            'user':Codigo,'senha':Senha,'valor':'erro'})
                
            ## verifica se o token atingiu a validade de 5 dias

            if tokendeautenticacao.fimValidadeToken() == True:

                return render(request, 'home/login.html',{'cad':"solicitacodigo",'hash':'solicitacodigo',
                                                        'user':Codigo,'senha':Senha}) 
            ## verifica se ja existe token para o usuario se não tiver cria
            if tokendeautenticacao.token() == False:

                if tokendeautenticacao.criarToken(tokendevalidacao) == True:

                    return render(request, 'home/login.html',{'cad':'login','user':Codigo,
                                                    'senha':Senha,'codigo_acesso':tokendevalidacao,'hash':validade_token.strftime("%d de %B")})
         
                else:

                    return render(request, 'home/login.html',{'usuario':""})

            return render(request, 'home/login.html',{'cad':"solicitacodigo",'hash':'solicitacodigo',
                                                        'user':Codigo,'senha':Senha})         
            
        return render(request, 'home/login.html',{'usuario':"usuário ou senha incorretos"})
  
    else:

        return render(request, 'home/login.html')

@login_required
def registraacesso(request):

   Codigo=request.user.username

   if Codigo:

    expires = datetime.strftime(
    datetime.utcnow() + timedelta(hours=10000000), "%a, %d-%b-%Y %H:%M:%S GMT")
    hoje = datetime.now(IST).date()
    

    idCookie=Codigo+hoje.strftime("%d%m%Y")
    stringMD5=MD5.converter(idCookie)
    UserMD5=MD5.converter(Codigo)
    codigoacesso=MD5.gerarhash()

    response = redirect(senha)
    
    if not request.COOKIES.get('usr'):

        response.set_cookie('usr', UserMD5,max_age=None,expires=expires)
        response.set_cookie('id', stringMD5,max_age=None,expires=expires) 

    
    tokendeautenticacao=tokendeAutenticacao(Codigo,hoje)

    if tokendeautenticacao.token() != False:

        tokendeautenticacao.contabilizaValidadeToken()
        tokendeautenticacao.criaNovoToken(codigoacesso)

        return response
        
    else:
           
           return redirect(home)
    
   return redirect(home)    

def cadastrar(request):
    
    codigo=request.POST.get("codigo")
    senha=request.POST.get("senha")
    cpf=request.POST.get("cpf")
    palavra_secreta = request.POST.get("email")
    hash_usuario = MD5.gerarhashCodBarras()

    if codigo:
      
      funcionariopdv=funcionarioPDV(codigo)
       
      if funcionariopdv.nome() != False:
       
        nome=funcionariopdv.nome()

        funcionario=Funcionario(nome)

        novoUsuario=usuarioTokenAuth(nome,codigo)

        if novoUsuario.usuario() != False:
        
             return render(request, 'cadastrar/index.html',{'errocadastrar':"usuário já cadastrado!"})
        
        if novoUsuario.cpf(cpf) != False:
            
            return render(request, 'cadastrar/index.html',{'errocadastrar':"CPF já cadastrado!"})

        if funcionario.ativo() == True:

            funcionario.alteraCPF(cpf)

            if novoUsuario.criarUsuario(cpf,senha,palavra_secreta,hash_usuario) == True:

                return render(request, 'cadastrar/index.html',{'cad':"sucesso_criar"})
            
            else:

                return render(request, 'cadastrar/index.html',{'usuario':"Não foi possivel realizar o cadastro"})                         
                      
        else:

            return render(request, 'cadastrar/index.html',{'errocadastrar':"Usuário inativo"})                       
      else:
         
        return render(request, 'cadastrar/index.html',{'errocadastrar':"Usuário de pdv inválido!"})
     
    else:
    
        return render(request, 'cadastrar/index.html')
    
@login_required
def senha(request):

    nome_usuario = funcionarioPDV(request.user.username).nome()
    hash_cod_barras = request.user.hash_usuario
    hoje = datetime.now(IST).date()
    aviso_validade_token = 5

    tokendeautenticacao=tokendeAutenticacao(request.user.username,hoje)
    funcionario=Funcionario(nome_usuario)

    if funcionario.funcionaro() == False:

        return render(request,'home/login.html',{'usuario':"Usuário não cadastrado para receber token"})
    
    tokensFuncionario=funcionario.tokensdoFuncionario()
    ##tokendb.listar(usuario.id,nome_usuario)
    codBarras.geraCodigo(funcionario.tokensdoFuncionario()['senhahoje'],hash_cod_barras)
    
    ontem = hoje - timedelta(1)
    anteontem = hoje - timedelta(2)

    data = {
    "nomeUsuario":nome_usuario,
    "ontem" : ontem.strftime("%d/%m/%Y"),
    "anteontem" : anteontem.strftime("%d/%m/%Y"),
    "imagem":"img/codBarras/"+hash_cod_barras+".svg"
    }

    if tokensFuncionario == "":
    
        return render(request,'home/login.html',{'usuario':"Usuário não cadastrado para receber token"})

    if str(tokendeautenticacao.token().data) != hoje.strftime("%Y-%m-%d"):

        if int(tokendeautenticacao.token().validade_token) == aviso_validade_token:

            return redirect(home)
        
        tokendeautenticacao.contabilizaValidadeToken()
        
    if int(tokendeautenticacao.token().validade_token) == aviso_validade_token:

        if tokendeautenticacao.token().data_ultimo_token != hoje.strftime("%Y-%m-%d"):
          
            return redirect(registraacesso)

        return render(request,'token/index.html',{'usuario':tokensFuncionario,'data':data,
                                                  'cad':'msg','codigo_acesso':tokendeautenticacao.token().proximo_token,
                                                  'hash':aviso_validade_token})

    return render(request,'token/index.html',{'usuario':tokensFuncionario,'data':data})

def alterarsenha(request):
     
    Codigo=request.POST.get("codigo")
    Cpf=request.POST.get("cpf")
    novasenha=request.POST.get("novasenha")
    hash=request.POST.get("hash")
    cad=request.POST.get("cad")
    validacaoemail=request.POST.get("validacaoemail")
    hoje = datetime.now(IST).date()

    if Codigo:

        hash_validacao=MD5.converter(f"{Codigo}{hoje}")
        funcionariopdv=funcionarioPDV(Codigo)
        usuarioTokenauth=usuarioTokenAuth(funcionariopdv.nome(),Codigo)
        tokendeautenticacao=tokendeAutenticacao(Codigo,hoje)
        funcionario=Funcionario(funcionariopdv.nome())


        if funcionario.funcionaro() != False:

            if usuarioTokenauth.cpf(Cpf) == False:

                return render(request, 'home/alterarsenha.html',{'retorno':"Os dados não correspodem"})

            if hash:
                
                if hash == hash_validacao:
            
                    usuarioTokenauth.alterarSenha(novasenha)

                    return render(request,'home/alterarsenha.html',{'cad':'sucesso'}) 
                
                if validacaoemail == '1':

                    if usuarioTokenauth.pinUsuario(hash) == False:
                        
                        return render(request, 'home/alterarsenha.html',
                                {'usuario_post':Codigo,'cpf':Cpf,'email':'1','valor':'erro',
                                'cad':'novasenha'})
                else:

                    if tokendeautenticacao.token().token_validacao != hash:

                        return render(request, 'home/alterarsenha.html',
                                    {'usuario_post':Codigo,'cpf':Cpf,'email':'email','valor':'erro',
                                    'cad':'novasenha'})
                
                return render(request, 'home/alterarsenha.html',{'usuario_post':Codigo,'cpf':Cpf,'cad':'senhanova',
                                                                'hash':hash_validacao,'pin':tokendeautenticacao.token().token_validacao})
            
            return render(request, 'home/alterarsenha.html',{'usuario_post':Codigo,'cpf':Cpf,
                                                            'email':'email','cad':'novasenha'})
        
        else:
             
             return render(request, 'home/alterarsenha.html',{'retorno':"Usuário não cadastrado para receber token"})

    
    return render(request,'home/alterarsenha.html')