/**
 * Created by s7eph4ni3 on 13-11-14.
 */
$(function(){
    $('#action-toggle').click(function(){
        if($(this).prop("checked")){
            $('.action-select').prop("checked",true);
        }else{
            $('.action-select').prop("checked",false);
        }
    });
    $('#go_page').click(function(){
        var go_page = $('.go_page').val();
        if (go_page != ''){
            window.location="/assets/iplist?page="+go_page;
        }else{
            alertify.alert("请输入页码！");
        }
    });
    $('#search').click(function(){
         var search_var= $('.search').val();
        if (search_var != ''){
            window.location="/assets/apisearchip?search_var="+search_var;
        }
    });
    $('#delip').click(function(){
        alertify.confirm("确定要删除?",function(e){
            if(e) {
                $(".action-select").each(function(){
                    if($(this).prop("checked")){
                        var thistmp = this;
                        $.get("/assets/apiipdel/"+$(this).val(),function(data){
                            data = JSON.parse(data);
                            if (data.code == 1) {
                                $(thistmp).parent().parent().remove();
                            }else if(data.code == 0){
                                alertify.alert("删除失败,"+data.message['auth']);
                            }
                        })
                    }
                });
                return true;
            } else {
                    return false;
            }
        });
    });
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
                $(".ip").text(data.message['ip']+data.message['iprang']);
                $(".idc").text(data.message['idc']);
                $(".auth").text(data.message['auth']);
                $("#ipsave").show();
                $(".iprang").text('填写格式:172.16.10.1-100');
            }
        }
    };
    // ajaxForm
    $("#ipform").ajaxForm(options);
    $("#iprangform").ajaxForm(options);
    $("#ipsave").click(function(){
        $(this).hide();
        $(".iprang").text('努力添加中。。。,请稍后！');
    });
    $(".del_ip").click(function(){
        var id = this.id;
        alertify.confirm("确定要删除?",function(e){
            if(e) {
                $.get("/assets/apiipdel/"+id,function(data){
                    data = JSON.parse(data);
                    if (data.code == 1) {
                        alertify.alert("删除成功");
                        $('#'+id).parent().parent().remove();
                    }else if(data.code == 0){
                        alertify.alert("删除失败,"+data.message['auth']);
                    }
                });
                return true;
            } else {
                return false;
            }
        });
    })
});