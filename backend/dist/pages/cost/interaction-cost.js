function getAllCost(data){
    // data: 一个空的json数据
    const response = fetch('/cost/get-all-cost',{
        method:'GET',
        headers:{
            'user-agent':'Mozilla/5.0',
            'Content-Type':'applications/json',
            'Accept':'Application/json'
        },
        credentials:'include',
        body:JSON.stringify(data)
    }).then(function (res){
        return res.json();
    })
    .then(function (res){
        return res;
    })
    return response;
}
function getCostByName(data){
    url = '../../../../cost/get-cost-by-name'
    if(Object.keys(data).length > 0){
        url = url + '?';
        var count = 0;
        var length = Object.keys(data).length;
        for(var i in data){
            url = url + i + '=' + data[i];
            count += 1;
            if(count != length){
                url = url + '&';
            }
        }
    }
    const response = await fetch(url,{
        method:'GET',
        headers:{
            'user-agent':'Mozilla/5.0',
            'Content-Type':'applications/json',
            'Accept':'Application/json'
        },
        mode:'no-cors',
        credentials:'include',
    }).then(function (res){
        return res.json();
    })
    .then(function (res){
        return res;
    })
    return response;
}
function newCost(data){
    const response =await fetch('/cost/new-cost',{
        method:'POST',
        headers:{
            'user-agent':'Mozilla/5.0',
            'Content-Type':'applications/json',
            'Accept':'Application/json'
        },
        credentials:'include',
        body:JSON.stringify(data)
    }).then(function(res){
        return res.json()
    }).then(function(res){
        return res;
    })
    return response;
}