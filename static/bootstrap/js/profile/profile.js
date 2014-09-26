/**
 * Created by s7eph4ni3 on 13-12-6.
 */
$(function () {
var options = {
    success: function (data) {
        data = JSON.parse(data);
        if (data.code == 1){
            $('#addidc').fadeOut();
            alertify.alert("添加成功");
            $('#alertify-ok').live("click",function(){
                window.location.assign(location);
            });
        }else if (data.code == 0){
            $(".username").text(data.message['username']);
            $(".first_name").text(data.message['first_name']);
            $(".password").text(data.message['password']);
            $(".email").text(data.message['email']);
            $(".last_name").text(data.message['last_name']);
            $(".auth").text(data.message['auth']);
        }
    }
};
// ajaxForm
$("#userform").ajaxForm(options);
});