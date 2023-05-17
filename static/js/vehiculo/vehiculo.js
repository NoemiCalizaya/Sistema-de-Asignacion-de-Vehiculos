function listadoVehiculos() {
    $.ajax({
        url: "/principal/listar/vehiculos",
        type: "get",
        dataType: "json",
        success: function (response) {
            $('#datatable-keytable').html("");
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]["fields"]['clase_vehiculo'] + '</td>';
                fila += '<td>' + response[i]["fields"]['marca'] + '</td>';
                fila += '<td>' + response[i]["fields"]['tipo_vehiculo'] + '</td>';
                fila += '<td>' + response[i]["fields"]['procedencia'] + '</td>';
                fila += '<td>' + response[i]["fields"]['modelo'] + '</td>';
                // fila += '<td>' + response[i]["fields"]['color'] + '</td>';
                // fila += '<td>' + response[i]["fields"]['placa'] + '</td>';
                // fila += '<td>' + response[i]["fields"]['cilindrada'] + '</td>';
                // fila += '<td>' + response[i]["fields"]['numero_motor'] + '</td>';
                // fila += '<td>' + response[i]["fields"]['numero_chasis'] + '</td>';
                // fila += '<td>' + response[i]["fields"]['estado_vehiculo'] + '</td>';
                // fila += '<td>' + response[i]["fields"]['observaciones'] + '</td>';
                fila += '<td><a href="/principal/detalle/' + response[i]['pk'] + '/vehiculo" class="btn btn-info" role="button"> DETALLE </a>';
                fila += '<a href="/principal/actualizar/' + response[i]['pk'] + '/vehiculo" class="btn btn-primary" role="button"> EDITAR </a>';
                fila += '<button type = "button" class = "btn btn-danger tableButton  btn-sm" ';
                fila += 'onclick = "abrir_modal_eliminacion(\'/principal/eliminar/' + response[i]['pk'] + '/vehiculo\');"> ELIMINAR </buttton></td>';
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
            setTimeout(() => { 
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
        url: '/principal/eliminar/'+pk+'/vehiculo',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoVehiculos();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}

$(document).ready(function () {
    listadoVehiculos();
    limMessErr();
});