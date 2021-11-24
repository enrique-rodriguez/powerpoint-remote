

window.addEventListener('load', function() {
    document.querySelectorAll(".btn").forEach((el) => {
        el.addEventListener('click', function(e) {
            let key = this.getAttribute('key');
            fetch(`${window.url}?key=${key}`, { method: 'POST'}).then((res) => {
                if(res.status != 200) {
                    alert("Could not connect to the server.")
                }
            })
        })
    })
})