async function getInventory(data){
    url = '../../../../warehouse/inventory'
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
    console.log(url);
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
        console.log(res)
        return res;
    })
    return response;
}
async function addInventory(data){
    const response =await fetch('/warehouse/new-inventory',{
        method:'POST',
        headers:{
            'user-agent':'Mozilla/5.0',
            'Content-Type':'applications/json',
            'Accept':'Application/json'
        },
        credentials:'include',
        body:JSON.stringify(data)
    });
    const answer = response.json()
    return answer;
}
async function modifyInventory(data){
    const response =await fetch('/warehouse/modify-inventory',{
        method:'POST',
        headers:{
            'user-agent':'Mozilla/5.0',
            'Content-Type':'applications/json',
            'Accept':'Application/json'
        },
        credentials:'include',
        body:JSON.stringify(data)
    });
    const answer = response.json()
    return answer;
}
async function deleteInventory(data){
    const response =await fetch('/warehouse/remove-inventory',{
        method:'DELETE',
        headers:{
            'user-agent':'Mozilla/5.0',
            'Content-Type':'applications/json',
            'Accept':'Application/json'
        },
        credentials:'include',
        body:JSON.stringify(data)
    });
    const answer = response.json()
    return answer;
}