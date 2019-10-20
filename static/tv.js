$(document).ready(function(){
    $(".folder").hide();
    $("#folder_text").hide();
    $("").hide();
    $("#tv").click(function() {
       $(".folder").show();
      });
    $("#movies").click(function() {
        $(".folder").hide();
        $("#folder_sel").hide();
        $("#folder_text").hide();
       });
    $("#new").click(function() {
        $("#folder_sel").hide();
        $("#folder_text").show();
       });
});