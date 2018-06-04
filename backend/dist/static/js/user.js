

var $form;
var form;
var $;
function updateValue(arg){
    $('#username').val(arg.username)
    $('#lastname').val(arg.lastname)
    $('#firstname').val(arg.firstname)
    $('#email').val(arg.email)
    $('#lastlogin').val(arg.lastlogin.substr(0,10) + ' '+arg.lastlogin.substr(11,8))
    $('#groups').val(arg.groups.toString())
    $('#datejoined').val(arg.datejoined.substr(0,10) + ' '+arg.datejoined.substr(11,8))
}
layui.use(['form','layer','upload','laydate'],function(){
	form = layui.form;
	var layer = parent.layer === undefined ? layui.layer : parent.layer;
		$ = layui.jquery;
		$form = $('form');
		laydate = layui.laydate;

        userInfo = {}

        $.ajax({
            url:'http://127.0.0.1:8000/user/getUser',  
            type:'POST',  //POST提交数据  
            xhrFields:{
                withCredentials:true
            },
            success:function(arg){  //请求成功后的回调函数。  
                //var obj = jQuery.parseJSON(arg); //解析后台返回数据
                if(arg.status==200){
                    userInfo = arg
                }else{
                    layer.msg('网络错误',{anim:5})
                }
            }, 
            async: false,
            error:function(){  //请求失败时调用此函数。  
                layer.msg('网络错误',{anim:5})
            }  
        });

        updateValue(userInfo)

        //添加验证规则
        form.verify({
            oldPwd : function(value, item){
                // var username = data.field.username
                // var password = data.field.password
                // // 如果登陆成功
                if(value == ""){
                    return "请输入旧密码！";
                }
            },
            newPwd : function(value, item){
                if(value.length < 8){
                    return "密码长度不能小于8位";
                }
            },
            confirmPwd : function(value, item){
                if(!new RegExp($("#newPwd").val()).test(value)){
                    return "两次输入密码不一致，请重新输入！";
                }
            }
        })


        //提交个人资料
        form.on("submit(changeUser)",function(data){
        	var index = layer.msg('提交中，请稍候',{icon: 16,time:false,shade:0.8});
            setTimeout(function(){
                layer.close(index);
                layer.msg("提交成功！");
            },2000);

            userInfo.firstname = $('#firstname').val()
            userInfo.lastname = $('#lastname').val()
            userInfo.email = $('#email').val()

            $.ajax({
                url:'http://127.0.0.1:8000/user/changeinfo',  
                type:'POST',  //POST提交数据  
                xhrFields:{
                    withCredentials:true
                },
                data:{
                    'newfirstname':userInfo.firstname,
                    'newlastname':userInfo.lastname,
                    'username':userInfo.username,
                    'newemail':userInfo.email
                },
                success:function(arg){  //请求成功后的回调函数。  
                    //var obj = jQuery.parseJSON(arg); //解析后台返回数据                  
                    if(arg.status!=200){
                        layer.msg('网络错误',{anim:5})
                    }
                }, 
                error:function(){  //请求失败时调用此函数。  
                    layer.msg('网络错误',{anim:5})
                }  
            });
            return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
        })

        // 取消修改用户信息
        form.on("submit(changePwd)",function(data){
            updateValue(userInfo)
            return false;
        })
        //修改密码
        form.on("submit(changePwd)",function(data){
        	var index = layer.msg('提交中，请稍候',{icon: 16,time:false,shade:0.8});

            var oldpassword = $('#oldPwd').val()
            var newpassword = $("#newPwd").val()

            $.ajax({
                url:'http://127.0.0.1:8000/user/changePassword',  
                type:'POST',  //POST提交数据  
                xhrFields:{
                    withCredentials:true
                },
                data:{
                    'oldpassword':oldpassword,
                    'newpassword':newpassword,
                    'username':userInfo.username
                },
                success:function(arg){  //请求成功后的回调函数。  
                    //var obj = jQuery.parseJSON(arg); //解析后台返回数据                  
                    if(arg.status==400){
                        layer.msg('旧密码错误',{anim:5})
                    }else if (arg.status ==200){
                        setTimeout(function(){
                            layer.close(index);
                            layer.msg("密码修改成功，请重新登陆");
                            $(".pwd").val('');
                            // parent.layer.close()
                        },1000);
                        parent.location.href='../../login.html'

                    }
                }, 
                error:function(){  //请求失败时调用此函数。  
                    layer.msg('网络错误',{anim:5})
                }  
            });
        	return false; //阻止表单跳转。如果需要表单跳转，去掉这段即可。
        })

        // 取消修改密码
        form.on("submit(cancelPwd)",function(data){
            $('#newPwd').text('')
            $('#oldPwd').text('')
            $('#confirmPwd').text('')
        })

})
