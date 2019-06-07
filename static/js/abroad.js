let map = tomtom.L.map('map', {
    key: 'Jvod0PUA0hjxGkT1AwIWJVdeGeV5pkr0',
    basePath: 'sdk',
    center: [21.689366, 12.657137],
    zoom: 1
});

let vaccines=["Гепатит B", "Дифтерія", "Кашлюк", "Правець", "Поліомієліт", "Гемофільна інфекція",
    "Кір",
    "Краснуха",
    "Паротит",
    "Туберкульоз",
    "Черевний тиф",
    "Сказ",
    "Жовта лихоманка",
    "Віспа"];



let countries = [
    // {
    //     "name": "Thailand",
    //     "lon": 15.639824,
    //     "lat": 101.036548
    // },
    {
        "name": "India",
        "lon": 22.444767,
        "lat": 79.679757
    },
    {
        "name": "Australia",
        "lon": -24.384835,
        "lat": 134.271366
    },
    {
        "name": "Mexico",
        "lon": 23.453923,
        "lat": -102.546908
    }
];
// let countries = [
//     {
//         "name": "India",
//         "lon": 22.444767,
//         "lat": 79.679757
//     },
//     {
//         "name": "Mexico",
//         "lon": 23.453923,
//         "lat": -102.546908
//     }
// ];


const getVaccs = async  () =>{
    let vaccs = [];
    //  vaccs.push(await getJSON("/" + "Mexico"));
    // vaccs.push(await getJSON("/" + "India" ));
    let c_coutn = countries;
    for(let i = 0; i < countries.length; i++){
        vaccs.push(await getJSON("/abroad/" + countries[i]["name"]));
    }
    // c_coutn.map(async x=> {vaccs.push(await getJSON("/" + x["name"]))});

    return vaccs;
};

const addMarkers = async () => {
    //await getJSON("/countries/" + x["name"])
    let c_vaccs = await getVaccs();
    console.log(c_vaccs);
    let arr = [];
    c_vaccs.map(x => {let y=""; x.map(d=>{y += vaccines[d["vacc_id"] - 1] + ", "});arr.push(y)});
    countries.map( (x) => tomtom.L.marker([x["lon"], x["lat"]]).addTo(map).bindPopup(arr[countries.indexOf(x)]));
};


addMarkers();