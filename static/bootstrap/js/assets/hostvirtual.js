/**
 * Created by s7eph4ni3 on 13-11-15.
 */
$(function(){
    $('#search').click(function(){
        var search_var= $('.search').val();
        if (search_var != ''){
            window.location="/assets/apisearchhostvirtual?search_var="+search_var;
        }else{
            alertify.alert("请输入主机名或ip");
        }
    });
});