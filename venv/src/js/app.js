const axios = require('axios');
const token = 'c1a5c9732610ed9b707a740e3136d14df768be1965fbf8d2fc8a2e67ba05a927'
const headers = {
    "Authorization": `Bearer ${token}`,
    'Accept-version': "3.0"
}

// let response = axios.get('')

function clear() {
    console.log('\033[2J');
}

const on_page = 50;

let upper = 0;
let lower = 0;
let ua = 0;


async function processData(url) {
    let data = await axios({
        method: 'get',
        headers: headers,
        url: url
    });
    // console.log('---\n', data.data.listings)
    for(let el of data.data.listings) {
        // console.log(el.shipping.rates)
        for(let rate of el.shipping.rates) {
            if(rate.region_code == 'XX' || rate.region_code == 'UA') {
                if(rate.region_code == 'UA') ua++;
                if(rate.rate.amount_cents >= 7500) upper++;
                else lower++;
            }
        }
    }
}

axios({
    method: 'get',
    headers: headers,
    url: 'https://api.reverb.com/api/listings?ships_to=UA&category=electric-guitars&page=1&per_page=5',
}).then(async data => {
    let total_pages = Math.floor(data.data.total/on_page);
    for(let i = 0; i < total_pages; i++) {
        await processData(`https://api.reverb.com/api/listings?ships_to=UA&category=electric-guitars&page=${i}&per_page=${on_page}`);
        clear()
        console.log(`${i}/${total_pages} processed`);
        console.log(`upper: ${upper} | lower: ${lower} | ua: ${ua}`);
    }
    console.log(`upper: ${upper} | lower: ${lower} | ua: ${ua}`);
}).catch(err => {
    console.log(err)
})
