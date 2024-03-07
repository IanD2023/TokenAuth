form_senhas=document.getElementById("form-senhas")
form_cadastrar=document.getElementById("form-cadastrar")
form_alterarsenha=document.getElementById("form-alterarsenha")

if (form_senhas){

document.getElementById("senhabarra").onclick = function() {codbarra()};

document.getElementById("senhas_anteriores").onclick = function() {senhas()};

}
function senhas() {
    
    document.getElementById("senhas").setAttribute("class", "d-flex justify-content-center");
    document.getElementById("botaovoltar").setAttribute("class", "d-flex justify-content-center");
    document.getElementById("usuario").setAttribute("class", "d-none ");
    document.getElementById("botoes").setAttribute("class", "d-none ");
      
}

function codbarra(){

    document.getElementById("codbarra").setAttribute("class", "container text-center"); 
    document.getElementById("senhanumero").setAttribute("class", "d-none");
    document.getElementById("senhabarra").setAttribute("class", "d-none");
    document.getElementById("senhanormal").setAttribute("class", "container text-center");
}

if (form_cadastrar || form_alterarsenha){

var password = document.getElementById("senha");
var confirm_password = document.getElementById("confirmarsenha");

function validarsenha(){
  if(password.value != confirm_password.value) {
    confirm_password.setCustomValidity("Senhas diferentes!");
  } else {
    confirm_password.setCustomValidity('');
  }
}

password.onchange = validarsenha;
confirm_password.onkeyup = validarsenha;

}