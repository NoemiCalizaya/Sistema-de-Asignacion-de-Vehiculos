function listadoAsignaciones() {
    $.ajax({
        url: "/asignacion/listar/asignaciones",
        type: "get",
        dataType: "json",
        success: function (response) {
            $('#datatable-keytable').html("");
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]['fields']['chofer_id'] + '</td>';
                fila += '<td>' + response[i]['fields']['vehiculo_id'][0] + '</td>';
                fila += '<td>' + response[i]['fields']['vehiculo_id'][1] + '</td>';
                fila += '<td>' + response[i]['fields']['unidad_id'] + '</td>';
                fila += '<td><button type="button" class="btn btn-success btn-sm tableButton"';
                fila += ' onclick="abrir_modal_detalle(\'/asignacion/detalle/' + response[i]['pk']+'/asignacion\');"><i class="fa fa-eye" aria-hidden="true"></i></button>';
                fila += '<a href="/asignacion/actualizar/' + response[i]['pk'] + '/asignacion" class="btn btn-primary" role="button"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Asignación</a>';
                fila += '<a href="/asignacion/devolucion/' + response[i]['pk'] + '/asignacion" class="btn btn-primary" role="button"><i class="fa fa-pencil-square-o" aria-hidden="true"></i> Devolución</a>';
                fila += '<button type="button" class="btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick="abrir_modal_eliminacion(\'/asignacion/eliminar/' + response[i]['pk'] + '/asignacion\');"><i class="fa fa-trash" aria-hidden="true"></i></button>';
                fila += '<a href="/asignacion/reporte/' + response[i]['pk'] + '/asignacion" class="btn btn-info" role="button" target="_blank"><i class="fa fa-file-pdf-o" aria-hidden="true"></i></a></td>';
                fila += '</tr>';
                $('#datatable-keytable').append(fila);
            }
            $('#datatable-keytable').DataTable({
                destroy: true,
                ordering : true,
                bPaginate: true,
                searching : true,
                language: {
                    "decimal": "",
                    "emptyTable": "No hay información",
                    "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
                    "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
                    "infoFiltered": "(Filtrado de _MAX_ total entradas)",
                    "infoPostFix": "",
                    "thousands": ",",
                    "lengthMenu": "Mostrar _MENU_ Entradas",
                    "loadingRecords": "Cargando...",
                    "processing": "Procesando...",
                    "search": "Buscar:",
                    "zeroRecords": "Sin resultados encontrados",
                    "paginate": {
                        "first": "Primero",
                        "last": "Ultimo",
                        "next": "Siguiente",
                        "previous": "Anterior"
                    },
                },
            });
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function registrar() {
    activarBoton();
    $.ajax({
        data: $('#form_creacion').serialize(),
        url: $('#form_creacion').attr('action'),
        type: $('#form_creacion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            limpiarForm();
            setTimeout(function() { 
                window.location.replace(response.url)
            }, 1800);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
    });
}

function editar() {
    activarBoton();
    var data = new FormData($('#form_edicion').get(0));
    $.ajax({        
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'), 
        data: data,
        cache: false,
        processData: false,
        contentType: false, 
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(function() { 
                window.location.replace(response.url)
            }, 1800);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        },        
    });
}

function editar_devolucion() {
    activarBoton();
    var data = new FormData($('#form_devolucion').get(0));
    $.ajax({      
        url: $('#form_devolucion').attr('action'),
        type: $('#form_devolucion').attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false, 
        success: function (response) {
            notificacionSuccess(response.mensaje);
            setTimeout(function() { 
                window.location.replace(response.url)
            }, 1800);
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        },        
    });
}

function eliminar(pk) {
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/asignacion/eliminar/'+pk+'/asignacion',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoAsignaciones();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}

$(document).ready(function () {
    listadoAsignaciones();
    limMessErr();
});