var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var componentId = this.dataset.product
        var action = this.dataset.action
        console.log('componentId: ', componentId, 'action:', action)
        console.log('USER:', user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
        }else{
            updateUserOrder(componentId, action)
    }})
}

function updateUserOrder (componentId, action) {
    console.log('User is logged in, sending data..')
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' :csrftoken,
        },
        body: JSON.stringify({'component_id': componentId, 'action': action})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}