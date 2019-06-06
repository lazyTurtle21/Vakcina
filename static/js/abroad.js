let map = tomtom.L.map('map', {
    key: 'Jvod0PUA0hjxGkT1AwIWJVdeGeV5pkr0',
    basePath: 'sdk',
    center: [21.689366, 12.657137],
    zoom: 1
});


let countries = [
    {
        "name": "Тайланд",
        "lon": 15.639824,
        "lat": 101.036548
    },
    {
        "name": "Індія",
        "lon": 22.444767,
        "lat": 79.679757
    },
    {
        "name": "Австралія",
        "lon": -24.384835,
        "lat": 134.271366
    },
    {
        "name": "Мексика",
        "lon": 23.453923,
        "lat": -102.546908
    }
];



const addMarkers = async () => {
    //await getJSON("/countries/" + x["name"])
    countries.map(async (x) => tomtom.L.marker([x["lon"], x["lat"]]).addTo(map).bindPopup("supercool"));
};


addMarkers();