var usuariocadastrado=document.getElementById("cadastrado");
var cadastro = document.getElementById("cad").value;

function convertMD5(codigo){
 
  hash = CryptoJS.MD5(codigo);

  return hash

}

const swalWithBootstrapButtons = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-success',
    cancelButton: 'btn btn-danger'
  },
  buttonsStyling: false
})

function modalalerta(titulo,mensagem,cor,icone){

  Swal.fire({
    position: 'center',
    icon: icone,
    title: titulo,
	text: mensagem,
    showConfirmButton:true,
    confirmButtonColor: cor,
	allowOutsideClick: false,
	allowEscapeKey: false,
    
  }).then((result) => {
    if (result.isConfirmed) {
        window.location.href="/"
    }
  })

}

if (cadastro == 'negado'){

  modalalerta('Acesso Negado','Este dispositivo está vinculado a outro usuário', '#d33','warning')

        } 

if (cadastro == 'logado') {

  modalalerta('Acesso Negado','Usuário logado em outro dispositivo!', '#d33','warning')
  
          }

if (cadastro == 'sucesso') {

  modalalerta('Sucesso','Senha alterada com sucesso!','green','success')
  
          }

if (cadastro == 'sucesso_criar') {

  modalalerta('Sucesso','Usuário cadastrado com sucesso!','green','success')
  
          }   
 
          

if (cadastro == "senhanova"){

  document.getElementById("container1").setAttribute("class", "justify-content-center");

}
          
if (cad.value == "3e1e53d67fb65cd1a6a425be4bba8e73"){

document.getElementById("container1").setAttribute("class", "justify-content-center");
document.getElementById("senha").setAttribute("required", "required");
document.getElementById("confirmarsenha").setAttribute("required", "required");

}  
