function listadoUnidades() {
    $.ajax({
        url: "/principal/listar/unidades",
        type: "get",
        dataType: "json",
        success: function (response) {
            // if ($.fn.DataTable.isDataTable('#datatable-keytable')) {
            //     $('#datatable-keytable').DataTable().destroy();
            // }
            console.log(response);
            $('#datatable-keytable').html("");
            for (let i = 0; i < response.length; i++) {
                let fila = '<tr>';
                fila += '<td>' + (i + 1) + '</td>';
                fila += '<td>' + response[i]['fields']['nombre_unidad'] + '</td>';
                fila += '<td>' + response[i]['fields']['secretaria_id'] + '</td>';
                fila += '<td><a href="/principal/actualizar/' + response[i]['pk'] + '/vehiculo" class="btn btn-primary" role="button"> EDITAR </a>';
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
            listadoUnidades();
            cerrar_modal_creacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
            mostrarErroresCreacion(error);
            activarBoton();
        }
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
    listadoUnidades();
});