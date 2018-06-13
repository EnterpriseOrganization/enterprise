function getInventory(data){
    const response = fetch('/warehouse/inventory',{
        method:'GET',
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
function addInventory(data){
    const response = fetch('/warehouse/new-inventory',{
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
function modifyInventory(data){
    const response = fetch('/warehouse/modify-inventory',{
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
function deleteInventory(data){
    const response = fetch('/warehouse/remove-inventory',{
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