let map;

const setLocation = (loc, geo) => {
    if (!geo.length) {
        geo.push(loc.coords.latitude);
        geo.push(loc.coords.longitude);
    }
    map = tomtom.L.map('map', {
        key: 'Jvod0PUA0hjxGkT1AwIWJVdeGeV5pkr0',
        basePath: 'sdk',
        center: geo,
        zoom: 13
    });
};

if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((loc) => {
            setLocation(loc, []);
        },
        (loc) => {
            setLocation(loc, [49.840838, 24.028037])
        });
} else {
    setLocation("", [49.840838, 24.028037]);
}


const isEmpty = (obj) => {
    for(let key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
};


const getCoordinates = async () => {
    let coors = await getJSON("/hospitals/" +
        document.getElementById("Info-block__search-form-input").value);
    console.log(typeof coors);
    if (isEmpty(coors)) return [];
    return [coors];
};


const initMap = async () => {
    console.log(document.getElementById("Info-block__search-form-input").value);
    let coordinates = await getCoordinates();

    document.getElementsByClassName("Search-form__text")[0].innerHTML =
        "Ми знайшли " + coordinates.length + " точок за вашим запитом.";

    coordinates.map((x) => tomtom.L.marker([x["long"], x["lat"]]).addTo(map).bindPopup(
        "Назва: " + x["name"] + "\nАдреса: " + x["address"] + "\nКількість вакцин: " + x["num_present"]));

    coordinates.map((x) => tomtom.L.marker([x["lon"], x["lat"]]).addTo(map).bindPopup(x["name"]));
};

