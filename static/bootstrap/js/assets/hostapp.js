/**
 * Created by s7eph4ni3 on 13-11-14.
 */
$(function(){
    $('.createvirtual').click(function(){
        $('#id_host').val(this.id);
    });
    var options = {
        success: function (data) {
            data = JSON.parse(data);
            if (data.code == 1){
                $('#addhostapp').fadeOut();
                alertify.alert("添加成功");
                $('#alertify-ok').live("click",function(){
                    window.location.reload();
                });
            }else if (data.code == 0){
                $(".name").text(data.message['name']);
                $(".host").text(data.message['host']);
                $(".ip_eth0").text(data.message['ip_eth0']);
                $(".hostgroup").text(data.message['hostgroup']);
                $(".business").text(data.message['business']);
                $(".user").text(data.message['user']);
                $(".auth").text(data.message['auth']);
            }
        }
    };
    var voptions = {
        success: function (data) {
            data = JSON.parse(data);
            if (data.code == 1){
                $('#addidc').fadeOut();
                alertify.alert("添加成功");
                $('#alertify-ok').live("click",function(){
                    window.location.reload();
                });
            }else if (data.code == 0){
                $(".vname").text(data.message['vname']);
                $(".vhost").text(data.message['vhost']);
                $(".ip_one").text(data.message['ip_one']);
                $(".vhostgroup").text(data.message['vhostgroup']);
                $(".vbusiness").text(data.message['vbusiness']);
                $(".vuser").text(data.message['vuser']);
                $(".auth").text(data.message['auth']);
            }
        }
    };
    // ajaxForm
    $("#hostappform").ajaxForm(options);
    $("#virtualhostform").ajaxForm(voptions);
    $('#go_page').click(function(){
        var go_page = $('.go_page').val();
        if (go_page != ''){
            window.location="/assets/hostapplist?page="+go_page;
        }else{
            alertify.alert("请输入页码！");
        }
    });
    $('#search').click(function(){
        var search_var= $('.search').val();
        if (search_var != ''){
            window.location="/assets/apisearchhostapp?search_var="+search_var;
        }else{
            alertify.alert("请输入主机名或IP");
        }
    });
});