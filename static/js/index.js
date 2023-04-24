function listadoPersonas(){
    $.ajax({
        url: "/principal/lista/personas",
        type: "get",
        dataType: "json",
        success: function(response){
            console.log(response);
            $('#datatable-keytable').html("");
            for(let i=0; i<response.length; i++){
                let fila = '<tr>';
                fila += '<td>'+(i+1)+'</td>';
                fila += '<td>'+response[i]["fields"]['ci']+'</td>';
                fila += '<td>'+response[i]["fields"]['nombres']+'</td>';
                fila += '<td>'+response[i]["fields"]['apellido_paterno']+'</td>';
                fila += '<td>'+response[i]["fields"]['direccion']+'</td>';
                fila += '<td><button type="button" class="btn btn-primary">EDITAR</button>';
                fila += '<button type="button" class="btn btn-danger"';
                fila += 'onclick="abrir_modal_eliminacion(\'/principal/eliminar/'+response[i]['pk']+'/persona\');">ELIMINAR</button></td>';
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

$(document).ready(function(){
    listadoPersonas();
});