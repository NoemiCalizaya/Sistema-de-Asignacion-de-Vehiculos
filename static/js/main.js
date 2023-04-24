var $ = jQuery.noConflict();
function abrir_modal_eliminacion(url){
    $('#eliminacion').load(url, function(){
        $(this).modal('show');
    });
}
