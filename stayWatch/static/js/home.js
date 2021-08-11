$(document).ready(function(){
    $("#nav-toggler").click(function(){
        $(".navbar .navbar-nav").toggleClass("navbar-nav-active");
    })
    var i=0;
    $("#nav-toggler").click(function(){

        i++;
      
        if(i%2==0)
        {
           console.log(i+"close");
           var open=document.getElementById("nav-toggler");
           open.innerHTML="<i class='bx bx-menu'></i>";
          
           
        }
        if(i%2!=0)
        {
            console.log(i+"open");
            var open=document.getElementById("nav-toggler");
            open.innerHTML="<i class='bx bx-x'></i>";
        }
    });
})