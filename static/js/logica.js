function eliminar_usuario(x) {
    id_usuario=x.value;
    form_eliminar=document.getElementById ("form_eliminar").action="/adm/usuario-eliminar/"+id_usuario+"/";

}

function ejecutar_eliminarf() {
    document.getElementById ("form_eliminar").submit();

}


/*function  editar_f ()
    id_usuario=x.value;
    form_editar0 doc*/





//
// function getdata() {
//   variable= $('#data').dataTable();
// comienzo de pagina
// }
