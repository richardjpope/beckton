$( document ).ready(function() {
  $(".meter.animate").each(function() {
    width = $(this).css('width')
    $(this).css('width', 0)
    $(this).animate({width: width}, 2000)
  });  
});
