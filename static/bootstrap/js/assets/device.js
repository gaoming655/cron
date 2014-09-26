/**
 * Created by s7eph4ni3 on 13-12-10.
 */
$(function(){
    $('#go_page').click(function(){
        var go_page = $('.go_page').val();
        if (go_page != ''){
            window.location="/assets/devicelist?page="+go_page;
        }else{
            alertify.alert("请输入页码！");
        }
    });
//    $('#search').click(function(){
//        var search_var= $('.search').val();
//        if (search_var != ''){
//            window.location="/assets/apisearchhost?search_var="+search_var;
//        }else{
//            alertify.alert("请输入SN或ilo ip");
//        }
//    });
});
$(function () {
        var options = {
            success: function (data) {
                data = JSON.parse(data);
                if (data.code == 1){
                    $('#addidc').fadeOut();
                    alertify.alert("添加成功");
                    $('#alertify-ok').live("click",function(){
                        window.location.reload();
                    });
                }else if (data.code == 0){
                    $(".device_type").text(data.message['device_type']);
                    $(".name").text(data.message['name']);
                    $(".sn").text(data.message['sn']);
                    $(".device_ip_one").text(data.message['device_ip_one']);
                    $(".brands").text(data.message['brands']);
                    $(".idc").text(data.message['idc']);
                    $(".mac").text(data.message['mac']);
                    $(".rack").text(data.message['rack']);
                    $(".position").text(data.message['position']);
                    $(".buy_time").text(data.message['buy_time']);
                    $(".supplier").text(data.message['supplier']);
                    $(".buy_price").text(data.message['buy_price']);
                    $(".auth").text(data.message['auth']);
                }
            }
        };
        // ajaxForm
        $("#deviceform").ajaxForm(options);
        $('#id_idc').change(function(){
           var csrftoken = $.cookie('csrftoken');
           var idc_var = $(this).val();
           $.post("/assets/apigetrack",{"idc":idc_var, csrfmiddlewaretoken: csrftoken},function(data){
               data = JSON.parse(data);
               if (data.code ==1){
                   $("#id_rack option").remove();
                   $('<option value="" selected="selected">---------</option>').prependTo('#id_rack');
                   for (var i=0;i< data.message.length;i++){
                       var html = '<option value="'+data.message[i].id+'">'+data.message[i].name+'</option>'
                       $(html).prependTo('#id_rack');
                   }
               }else{
                   $("#id_rack option").remove();
                   $('<option value="" selected="selected">---------</option>').prependTo('#id_rack');
               }
           });
       });
       $('#id_rack').change(function(){
           var csrftoken = $.cookie('csrftoken');
           var rack_var = $(this).val();
           $.post("/assets/apigetposition",{"rack":rack_var, csrfmiddlewaretoken: csrftoken},function(data){
               data = JSON.parse(data);
               if (data.code ==1){
                   $("#id_position option").remove();
                   $('<option value="" selected="selected">---------</option>').prependTo('#id_position');
                   for (var i=0;i< data.message.length;i++){
                       var html = '<option value="'+data.message[i].id+'">'+data.message[i].name+'</option>'
                       $(html).prependTo('#id_position');
                   }
               }else{
                   $("#id_position option").remove();
                   $('<option value="" selected="selected">---------</option>').prependTo('#id_position');
               }
           });
       });
});
