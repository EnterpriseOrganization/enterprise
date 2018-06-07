layui.extend({
    admin: '{/}../../static/js/admin'
});

layui.use(['table', 'jquery','form', 'admin'], function() {
    var table = layui.table,
        $ = layui.jquery,
        form = layui.form,
        admin = layui.admin;

    table.render({
        elem: '#orderList',
        cellMinWidth: 100,
        cols: [
            [{
                type: 'checkbox'
            }, {
                field: 'id',title: '订单编号',sort: true,width:180
            }, {
                field: 'name',title: '货品名称',sort: true,width:150
            }, {
                field: 'number',title: '数量',sort:true,width:80
            },  {
                field: 'price',title: '订单金额',sort:true
            }, {
                field: 'date',title: '交付时间',sort: true,width:150
            },{
                field: 'person',title: '订货人'
            }, {
                field: 'status',title: '订单状态',toolbar: '#statusTpl'
            }, {
                field: 'operate',title: '操作',toolbar: '#operateTpl',unresize: true
            }]
        ],
        data: [{
            "id": "2017009171822298053",
            "name": "EB23下电板EPL",
            "number": "10000",
            "date": "2017-08-17 18:22",
            "price": "1234.34",
            "person": "吴彦祖",
            "status": "已完成"
        }, {
            "id": "2017009171822298053",
            "name": "EB23下电板EPL",
            "number": "10000",
            "date": "2017-08-17 18:22",
            "price": "1234.34",
            "person": "吴彦祖",
            "status": "未完成"
        }],
        event: true,
        page: true
    });
    /*
     *数据表格中form表单元素是动态插入,所以需要更新渲染下
     * http://www.layui.com/doc/modules/form.html#render
     * */
    $(function(){
        form.render();
    });

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