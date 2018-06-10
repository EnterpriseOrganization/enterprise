layui.extend({
    admin: '{/}../../static/js/admin'
});

layui.use(['table', 'jquery','form', 'admin'], function() {
    var table = layui.table,
        $ = layui.jquery,
        form = layui.form,
        admin = layui.admin;
        mdata = null;

    table.render({
        elem: '#orderList',
        cellMinWidth: 100,
        id: 'id',
        cols: [
            [{
                type: 'checkbox'
            }, {
                field: 'id',title: '订单编号',sort: true,width:180
            },  {
                field: 'price',title: '订单金额',sort:true
            }, {
                field: 'start_date',title: '下单',sort: true,width:150
            },{
                field: 'end_date',title: '交付日期',sort: true,width:150
            },{
                field: 'indentor',title: '订货商'
            }, {
                field: 'status',title: '订单状态',sort: true
            }, {
                field: 'operate',title: '操作',toolbar: '#operateTpl',unresize: true
            }]
        ],
        data: mdata,
        
        event: true,
        page: true
    });

    var req = 'get-all-order'
        var pdata
        var kdata = []
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/order/" + req,
            cache: false,
            async: false,
            contenType: "application/json",
            dataType: "json",
            success: function(data) {
                pdata = data;
                pdata = JSON.parse(pdata)
                console.log(pdata)

                for(var i in pdata) {
                    var status
                    if(pdata[i].fields.status) status = "已完成"
                    else status = "未完成"
                    kdata[i] = {
                        "id": pdata[i].pk,
                        "price": pdata[i].fields.totalprice,
                        "start_date": pdata[i].fields.date.substr(0, 9),
                        "end_date": pdata[i].fields.deliverydate.substr(0, 9),
                        "indentor": pdata[i].fields.indentor,
                        "status": status
                    }
                }
                
                table.reload('id', {
                        data : kdata
                })
            },
            error: function (err) {
                console.log(err);
            }
        })
    
    /*
     *数据表格中form表单元素是动态插入,所以需要更新渲染下
     * http://www.layui.com/doc/modules/form.html#render
     * */
    $(function(){
        form.render();
    });
    function getListInfo() {
        
        return pdata;
    }
    var active = {
        getCheckData: function() { //获取选中数据
            var checkStatus = table.checkStatus('orderList'),
                data = checkStatus.data;
            //console.log(data);
            //layer.alert(JSON.stringify(data));
            if(data.length > 0) {
                layer.confirm('确认要删除吗？' + JSON.stringify(data), function(index) {
                    layer.msg('删除成功', {
                        icon: 1
                    });
                    //找到所有被选中的，发异步进行删除
                    $(".layui-table-body .layui-form-checked").parents('tr').remove();
                });
            } else {
                layer.msg("请先选择需要删除的文章！");
            }

        },
        Recommend: function() {
            var checkStatus = table.checkStatus('orderList'),
                data = checkStatus.data;
            if(data.length > 0) {
                layer.msg("您点击了推荐操作");
                for(var i = 0; i < data.length; i++) {
                    console.log("a:" + data[i].recommend);
                    data[i].recommend = "checked";
                    console.log("aa:" + data[i].recommend);
                    form.render();
                }

            } else {
                console.log("b");
                layer.msg("请先选择");
            }

            //$(".layui-table-body .layui-form-checked").parents('tr').children().children('input[name="zzz"]').attr("checked","checked");
        },
        Top: function() {
            layer.msg("您点击了置顶操作");
        },
        Review: function() {
            layer.msg("您点击了审核操作");
        }

    };

    $('.demoTable .layui-btn').on('click', function() {
        var type = $(this).data('type');
        active[type] ? active[type].call(this) : '';
    });

    /*用户-删除*/
    window.member_del = function(obj, id) {
        layer.confirm('确认要删除吗？', function(index) {
            //发异步删除数据
            $(obj).parents("tr").remove();
            layer.msg('已删除!', {
                icon: 1,
                time: 1000
            });
        });
    }

});

function delAll(argument) {
    var data = tableCheck.getData();
    layer.confirm('确认要删除吗？' + data, function(index) {
        //捉到所有被选中的，发异步进行删除
        layer.msg('删除成功', {
            icon: 1
        });
        $(".layui-form-checked").not('.header').parents('tr').remove();
    });
}