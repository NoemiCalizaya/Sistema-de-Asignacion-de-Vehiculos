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

function limpiarForm(){
	document.getElementById("form_creacion").reset();
}

function limMessErr(){
	$("input").change(function (e) { 
        let element = document.getElementById(e.target.id);
        if (element.nextElementSibling != null){
            element.nextElementSibling.remove();
        }
    });
}

function limpiarEdicion(){
	$("div").remove(".error");
}

function mostrarErrores(er, formulario){
	$("div").remove(".error");
	for(let item in er){
		let idElemento = formulario.elements[item].id;
		let element = document.getElementById(idElemento);
		let newElement = document.createElement('div');
		let text = er[item];
		let newContent = document.createTextNode(text);
  		newElement.appendChild(newContent); //añade texto al div creado.
		newElement.className = 'error';
		newElement.style.color = 'red';
		let elementParent = element.parentNode;
		elementParent.insertBefore(newElement, idElemento.nextSibling);
	}
}

function mostrarErroresCreacion(errores){
	let miformulario = document.getElementById("form_creacion");
	mostrarErrores(errores.responseJSON.error, miformulario)
}

function mostrarErroresEdicion(errores) {
	let miformulario = document.getElementById("form_edicion");
	mostrarErrores(errores.responseJSON.error, miformulario)
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
