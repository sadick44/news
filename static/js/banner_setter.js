$(document).ready(function(){
    var counter = 1;
    setInterval(()=>{
        if(counter > 4){
            counter = 1;
        }
        current_image = $('#banner'+counter).attr('src');
        $('#main_display').attr('src', current_image);
        counter += counter;
    }, 3000)
})