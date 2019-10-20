$(document).ready(function(){
$(".folder").hide();
$("#folder_text").hide();
});
function tv_sel(val) {
    if(val==0){
        $(".folder").show();
    }
    else if(val==1){
        $(".folder").hide();
        $("#folder_sel").hide();
        $("#folder_text").hide();
    }
}
function createNew(len,index) {
    if(index == len-1){
        $("#folder_sel").hide();
        $("#folder_text").show();
    }
}


