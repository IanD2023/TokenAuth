//Validação de email

var nome_email = document.getElementById("email-validacao");
var cod_auth_email= document.getElementById("hash");
var cad = document.getElementById("cad");
var submit = document.getElementById("botao-submit");
var usuario=document.getElementById("codigo");

function login(titulo,texto,botaoclick,redirect,cod_auth_email){

  Swal.fire({

    title: titulo,
    text:texto,
    input: 'text',
    inputAttributes: {
      autocapitalize: 'off'
    },
    showCancelButton: true,
    cancelButtonText: 'cancelar',
    cancelButtonColor: '#6e7881',
    confirmButtonText: 'ok',
    confirmButtonColor: 'green',
    showLoaderOnConfirm: true,
	allowOutsideClick: false,
	allowEscapeKey: false,

  preConfirm: (login) => {

        cod_auth_email.setAttribute("value", login);
        
        botaoclick.click();
  }
  }).then(function(result){
       
        if(result.dismiss == 'cancel'){

          window.location.href=redirect
      }

    });

    if (submit.value == 'erro'){

      Swal.showValidationMessage(
  
        'O código informado não corresponde.'
      )
    }
  
  }

    function alterarsenha(titulo,nome_email,texto,botaoclick,redirect,cod_auth_email){

      Swal.fire({
    
        title: titulo,
        text:texto,
        input: 'text',
        inputAttributes: {
          autocapitalize: 'off'
        },
        showCancelButton: true,
        cancelButtonText: 'Não tenho o código',
        cancelButtonColor: '#6e7881',
        confirmButtonText: 'ok',
        confirmButtonColor: 'green',
        showDenyButton: true,
        denyButtonText: 'cancelar',
        denyButtonColor: 'red',
        showLoaderOnConfirm: true,
      allowOutsideClick: false,
      allowEscapeKey: false,
    
      preConfirm: (login) => {
    
            cod_auth_email.setAttribute("value", login);
            
            botaoclick.click();
      }
      }).then(function(result){
            if(result.isDenied ){
              window.location.href=redirect
            }
           
            if(result.dismiss == 'cancel'){
    
               nome_email.setAttribute("value", '1');
    
               alterarsenha('Liberar Acesso',nome_email,'Utiliza a palavra secreta informada no cadastro',submit,"/usr",cod_auth_email)
    
          }
    
        });

  if (submit.value == 'erro'){

    Swal.showValidationMessage(

      'O código informado não corresponde.'
    )
  }

}

function codigoAcesso(titulo,nome_email,botaoclick,redirect,cod_auth_email,cor){

  Swal.fire({

    title: titulo,
    icon: 'info',
    html:nome_email,
    confirmButtonText: 'Ok',
    confirmButtonColor: cor,
    showLoaderOnConfirm: true,
	allowOutsideClick: false,
	allowEscapeKey: false,

  preConfirm: (login) => {

        cod_auth_email.setAttribute("value", titulo);

        if (botaoclick != false){
        
        botaoclick.click();
        }
  }
  })

}

if (cad.value == "login"){

  codigoAcesso(nome_email.value,'GUARDE ESTE CÓDIGO</br>ele será solicitado para autenticar seu acesso nos próximos 5 dias.',submit,"/",cod_auth_email,'#3085d6')

}


if (cad.value == "msg"){

  codigoAcesso(nome_email.value,'a partir de amanhã este será seu novo código de autenticação.',false,"",cod_auth_email,'#3085d6')

}

if (cad.value == "solicitacodigo"){

  login('Liberar Acesso','Informe o código de autenticação',submit,"/",cod_auth_email)

}

if (cad.value == "novasenha"){

  alterarsenha('Liberar Acesso',nome_email,'Informe o código de autenticação',submit,"/usr",cod_auth_email)

}

if (nome_email.value == "1"){

  alterarsenha('Liberar Acesso',nome_email,'Utiliza a palavra secreta informada no cadastro',submit,"/usr",cod_auth_email)

}