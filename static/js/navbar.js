// Fuction of hidde and show menú in a pc or mobile 
let btnClose, btnOpen;
if (document.body.clientWidth <= 650){
    //console.log('Es pequeña');
    btnClose = document.getElementsByClassName('btn-menu-mobile');
    btnOpen = document.getElementsByClassName('btn-menu');
}
else{
    //console.log('Es grande');
    btnClose = document.getElementsByClassName('btn-menu');
}
let menu = document.getElementsByClassName('navbar');
//console.log(btnClose);
Array.from(btnClose).forEach((element, index)=>{
    element.addEventListener('click',()=>{
        //console.log('Si');
        if(document.body.clientWidth <= 650){
            menu[0].classList.toggle('navbar-show');
            btnOpen[0].classList.toggle('btn-menu-hidden');
        }
        else{
            menu[0].classList.toggle('navbar-show');
        }
    });
});
if(document.body.clientWidth <= 650){
    Array.from(btnOpen).forEach((element, index)=>{
        element.addEventListener('click',()=>{
            console.log('Si');
            element.classList.toggle('btn-menu-hidden');
            menu[0].classList.toggle('navbar-show');
            });
        });
}