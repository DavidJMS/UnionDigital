/*                      Controls to hidde message error                         */

btnCloseMessageError = document.getElementById("close-message-error");
btnOpenMessageError = document.getElementById("open-message-error");
messageError = document.getElementById("messageError");
//Event click in buttons:
btnCloseMessageError.addEventListener('click',(e)=>{
    messageError.classList.remove("animate__slideInDown");
    messageError.classList.add("animate__slideOutUp");
    btnOpenMessageError.classList.remove("btn-error-hidde");
});
btnOpenMessageError.addEventListener('click',(e)=>{
    btnOpenMessageError.classList.add("btn-error-hidde");
    messageError.classList.remove("animate__slideOutUp");
    messageError.classList.add("animate__slideInDown");
});