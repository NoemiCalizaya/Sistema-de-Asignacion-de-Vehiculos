var $ = jQuery.noConflict();

function abrir_modal_creacion(url) {
	$('#creacion').load(url, function () {
		$(this).modal('show');
	});
}

function cerrar_modal_creacion(){
	$('#creacion').modal('hide');
}

function abrir_modal_detalle(url) {
	$('#detalle').load(url, function () {
		$(this).modal('show');
	});
}

function cerrar_modal_detalle(){
	$('#detalle').modal('hide');
}

function abrir_modal_edicion(url) {
	$('#edicion').load(url, function () {
		$(this).modal('show');
	});
}
function cerrar_modal_edicion() {
	$('#edicion').modal('hide');
}

function abrir_modal_eliminacion(url){
    $('#eliminacion').load(url, function(){
        $(this).modal('show');
    });
}
function cerrar_modal_eliminacion() {
	$('#eliminacion').modal('hide');
}

function activarBoton(){
	if($('#boton_creacion').prop('disabled')){
		$('#boton_creacion').prop('disabled',false);
	}else{
		$('#boton_creacion').prop('disabled', true);
	}
}

function mostrarErroresCreacion(errores){
	$('#errores').html("");
	let error = "";
	for(let item in errores.responseJSON.error){
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#errores').append(error);
}

function mostrarErroresEdicion(errores) {
	$('#erroresEdicion').html("");
	let error = "";
	for (let item in errores.responseJSON.error) {
		error += '<div class = "alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>';
	}
	$('#erroresEdicion').append(error);
}

function notificacionSuccess(mensaje) {
	Swal.fire({
		title: 'Buen Trabajo!',
		text: mensaje,
		icon: 'success'
	})
}

function notificacionError(mensaje){
	Swal.fire({
		title: 'Error!',
		text: mensaje,
		icon: 'error'
	})
}
