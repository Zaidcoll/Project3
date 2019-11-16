/* global $*/

$(function(){
    $('select').material_select();
    $(".button-collapse").sideNav();
    $('.collapsible').collapsible();
    $('.carousel.carousel-slider').carousel({fullWidth: true});
    $('.slider').slider();


$('#MCD').on('click', function() {
    $('.MC').css('display','block')
    $('.KFC, .PIZZA, .BURGER').css('display','none')
    });
    
$('#KFC').on('click',function(){
    $('.KFC').css('display','block')
    $('.MC, .PIZZA, .BURGER').css('display','none')
    });

$('#BURGER').on('click',function(){
    $('.BURGER').css('display','block')
    $('.MC, .PIZZA, .KFC').css('display','none')
    });

$('#PIZZA').on('click',function(){
    $('.PIZZA').css('display','block')
    $('.MC, .BURGER, .KFC').css('display','none')
    });

$('#ALL').on('click',function(){
    $('.MC, .BURGER, .KFC, .PIZZA').css('display','block')
    });
    
})

