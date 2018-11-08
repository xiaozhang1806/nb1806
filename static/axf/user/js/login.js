$(function () {
    $("#submit").click(login);
})
function login() {
    var name = $("#uid").val();
    var pwd = $("#u_pwd").val();

    if (name.length < 3) {
        alert("用户名过短");
        return;
    }
    if (pwd.length < 6) {
        alert("密码过短");
        return;
    }

    var enc_pwd = md5(pwd);

    $.ajax({
        url: "/appaxfs/login",
        data: {
            "name": name,
            "pwd": enc_pwd
        },
        method: "post",
        success: function (res) {

            if (res.code == 1) {
                window.open(res.data, target = "_self");
            } else {
                alert(res.msg);
            }
        },
        error: function () {

        },
        complete: function () {

        }
    });
}
