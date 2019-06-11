window.onload = function() {
    let app = new Vue({
        name: 'div-id-app',
        el: '#app',
        data: {
            message: 'asd',
            thomann_price: ''
        },
        methods: {
            getPrice() {
                fetch(`/estimated_price?price=${this.thomann_price}`)
                    .then(data => {                        
                        console.log(this.thomann_price)
                        console.log('message:', data.message)
                    })
                    .catch(err => {
                        alert('err')
                    })
            }
        },
        delimiters: ['[[',']]']
    })
}