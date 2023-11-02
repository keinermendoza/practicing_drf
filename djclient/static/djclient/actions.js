document.addEventListener('DOMContentLoaded', () => {
    const BaseUrl = 'http://localhost:8000/api/v1/products/' 
    const resultsTarget = document.getElementById('results')

    // get all
    document.getElementById('get-all').onclick = () => {
        fetch(BaseUrl)
        .then(res => res.json())
        .then(data => showProduct(data, resultsTarget))
        .catch(err => console.log(err))
    }

    // get one
    document.getElementById('get-one').onsubmit = function(e) {
        e.preventDefault()
        fetch(`${BaseUrl}${this.pk.value}`)
        .then(res => {
            if (res.ok) {this.reset()}
            return res.json()
        })
        .then(data => resultsTarget.innerHTML = JSON.stringify(data))    
        .catch(err => console.log(err))
    }

    // post 
    document.getElementById('post').onsubmit = function(e) {
        e.preventDefault()
        fetchPostAndPut(BaseUrl, this, resultsTarget)
    }

    // put 
    document.getElementById('put').onsubmit = function(e) {
        e.preventDefault()
        fetchPostAndPut(BaseUrl, this, resultsTarget, this.pk.value)
    }

    // delete
    document.getElementById('delete').onsubmit = function(e) {
        e.preventDefault()
        fetch(`${BaseUrl}${this.pk.value}`, {
            method: 'delete',
            headers: {
                'X-CSRFToken': this.csrfmiddlewaretoken.value,
                'Content-Type': 'application/json',
            },
        })
        .then(res => resultsTarget.innerHTML = JSON.stringify(res.status))
        .catch(err => console.log(err))
    }
})


// for post and put
function fetchPostAndPut(url, form, parent, product_id=null) {
    
    const finalUrl = product_id ? url + product_id : url;
    fetch(finalUrl, {
        method: product_id ? 'PUT': 'POST',
        headers: {
            'X-CSRFToken': form.csrfmiddlewaretoken.value,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            title: form.title.value,
            content: form.content.value,
            price: form.price.value,   
        }),
    })
    .then(res => res.json())
    .then(data => parent.innerHTML = JSON.stringify(data))    
    .catch(err => console.log(err))
}

// for get all
function showProduct(data, parent) {
    parent.innerHTML = data.map(element => {
        return(
        `
    <div style="margin-block:50px;">
        <p>id: ${element.id}</p>
        <h4>${element.title}</h4>
        <p>Content: ${element.content}</p>
        <p>Price: $ ${element.price}</p>
    </div>
        `)
    }).join("")
}