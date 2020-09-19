/*                  Controls to slice efect in forms                */

divToHidde = Array.from(document.getElementsByClassName('slash-efect'));
divShowed = document.getElementsByClassName('slash-efect-show');
hiddeLeftButton = document.getElementById('right');
hiddeRightButton = document.getElementById('left');

let index = 0;

//Events in buttons
hiddeLeftButton.addEventListener('click',(e)=>{
    if(index<divToHidde.length-1){
        index++; 
        hiddeToLeft(index,divToHidde);
    }
});

hiddeRightButton.addEventListener('click',(e)=>{
    if(index>0){
        index--; 
        hiddeToRight(index,divToHidde);
    }
});

//Functions hidde
function hiddeToLeft(index,array){
    divShowed[0].classList.add("slash-efect-hidde-left");
    divShowed[0].classList.remove("slash-efect-show");
    array[index].classList.remove("slash-efect-hidde-right");
    array[index].classList.add('slash-efect-show');
}

function hiddeToRight(index,array){
    divShowed[0].classList.add("slash-efect-hidde-right");
    divShowed[0].classList.remove("slash-efect-show");
    array[index].classList.remove("slash-efect-hidde-left");
    array[index].classList.add('slash-efect-show');
}
