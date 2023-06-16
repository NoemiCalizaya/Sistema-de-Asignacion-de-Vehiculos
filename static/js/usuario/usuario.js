function listadoUsuarios(){
    $.ajax({
        url: "/usuario/lista/usuarios",
        type: "get",
        dataType: "json",
        success: function(response){
            $('#datatable-keytable').html("");
            for(let i=0; i<response.length; i++){
                let fila = '<tr>';
                fila += '<td>'+(i+1)+'</td>';
                fila += '<td>'+response[i]["fields"]['first_name']+'</td>';
                fila += '<td>'+response[i]["fields"]['last_name']+'</td>';
                fila += '<td>'+response[i]["fields"]['email']+'</td>';
                fila += '<td>'+response[i]["fields"]['username']+'</td>';
                if (response[i]["fields"]['is_active']){
                    response[i]["fields"]['is_active'] = "activo";
                    fila += '<td>'+response[i]["fields"]['is_active']+'</td>';
                }
                else{
                    response[i]["fields"]['is_active'] = "inactivo";
                    fila += '<td>'+response[i]["fields"]['is_active']+'</td>';
                }
                fila += '<td><button type="button" class="btn btn-primary btn-sm tableButton"';
                fila += ' onclick="abrir_modal_edicion(\'/usuario/editar/'+ response[i]['pk']+'/usuario\');"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></button>';
                fila += '<button type="button" class = "btn btn-danger btn-sm tableButton"';
                fila += ' onclick="abrir_modal_eliminacion(\'/usuario/eliminar/' + response[i]['pk']+'/usuario\');"><i class="fa fa-trash" aria-hidden="true"></i></button></td>';
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

function editar(){
    activarBoton();
    $.ajax({
        data: $('#form_edicion').serialize(),
        url: $('#form_edicion').attr('action'),
        type: $('#form_edicion').attr('method'),
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoUsuarios();
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
        url: '/usuario/eliminar/'+pk+'/usuario',
        type: 'post',
        success: function (response) {
            notificacionSuccess(response.mensaje);
            listadoUsuarios();
            cerrar_modal_eliminacion();
        },
        error: function (error) {
            notificacionError(error.responseJSON.mensaje);
        }
    });
}

$(document).ready(function(){
    listadoUsuarios();
    limMessErr();
});