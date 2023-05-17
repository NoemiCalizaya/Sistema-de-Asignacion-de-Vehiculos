function listadoChoferes(){
    $.ajax({
        url: "/principal/lista/choferes",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#datatable-keytable').html("");
            for(let i=0; i<response.length; i++){
                let fila = '<tr>';
                fila += '<td>'+(i+1)+'</td>';
                fila += '<td>'+response[i]["fields"]['ci']+'</td>';
                fila += '<td>'+response[i]["fields"]['nombres']+'</td>';
                fila += '<td>'+response[i]["fields"]['apellido_paterno']+'</td>';
                if (response[i]["fields"]['apellido_materno'] === null){
                    response[i]["fields"]['apellido_materno'] = " ";
                    fila += '<td>'+response[i]["fields"]['apellido_materno']+'</td>';
                }
                else
                    fila += '<td>'+response[i]["fields"]['apellido_materno']+'</td>';
                fila += '<td>'+response[i]["fields"]['categoria_lic']+'</td>';
                fila += '<td><button type = "button" class="btn btn-info btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_detalle(\'/principal/detalle/' + response[i]['pk']+'/chofer\');"> DETALLE </button>';
                fila += '<button type = "button" class = "btn btn-primary btn-sm tableButton"';
                fila += ' onclick = "abrir_modal_edicion(\'/principal/actualizar/' + response[i]['pk']+'/chofer\');"> EDITAR </button>';
                fila += '<button type="button" class="btn btn-danger"';
                fila += 'onclick="abrir_modal_eliminacion(\'/principal/eliminar/'+response[i]['pk']+'/chofer\');">ELIMINAR</button></td>';
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
                    }
                },
        
            });
        },
        error: function(error){
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
            listadoChoferes();
            cerrar_modal_creacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
    });
}

function editar(){
    activarBoton();
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoChoferes();
            cerrar_modal_edicion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresEdicion(error);
            activarBoton();
        }
    });
}

function eliminar(pk) {
    $.ajax({
        data:{
            csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
        },
        url: '/principal/eliminar/'+pk+'/chofer',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoChoferes();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}

$(document).ready(function(){
    listadoChoferes();
    limMessErr();
});