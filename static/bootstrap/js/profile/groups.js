/**
 * Created by s7eph4ni3 on 13-12-6.
 */
$(function(){
    $('#id_permissions_add_all_link').click(function(){
        var html = $('#id_permissions_from option');
        $('#id_permissions_to').append(html);
        $("#id_permissions_to").find("option").attr("SELECTED",true);
    });
    $('#id_permissions_remove_all_link').click(function(){
        var html = $('#id_permissions_to option');
        $('#id_permissions_from').append(html);
        $("#id_permissions_from").find("option").attr("SELECTED",false);
    });
    $('#id_permissions_add_link').click(function(){
        var html = $('#id_permissions_from option:selected');
        $('#id_permissions_to').append(html);
    });
    $('#id_permissions_remove_link').click(function(){
        var html = $('#id_permissions_to option:selected');
        $('#id_permissions_from').append(html);
        $("#id_permissions_from option:selected").attr("SELECTED",false);
    });
    $('#id_permissions_from option').dblclick(function(){
        $('#id_permissions_to').append(this);
    });
    $('#id_permissions_to').dblclick(function(){
        var html = $('#id_permissions_to option:selected');
        $('#id_permissions_from').append(html);
        $("#id_permissions_from option:selected").attr("SELECTED",false);
    });
    var options = {
        success: function (data) {
            data = JSON.parse(data);
            if (data.code == 1){
                $('#addidc').fadeOut();
                alertify.alert("修改成功");
                $('#alertify-ok').live("click",function(){
                    window.location.assign(location);
                });
            }else if (data.code == 0){
                $(".name").text(data.message['name']);
                $(".permissions").text(data.message['permissions']);
                $(".auth").text(data.message['auth']);
            }
        }
    };
    // ajaxForm
    $("#groupsform").ajaxForm(options);
});