let map;
let lviv_center = [49.840838, 24.028037];

const setLocation = (loc, geo) => {
    if (!geo.length){
        geo = [loc.coords.latitude, loc.coords.longitude]
    }
    map = tomtom.L.map('map', {
        key: 'Jvod0PUA0hjxGkT1AwIWJVdeGeV5pkr0',
        basePath: 'sdk',
        center: geo,
        zoom: 13
    });
};


if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition((loc) => {setLocation(loc, []);},
        (loc) => {setLocation(loc, lviv_center)});
} else{
    setLocation("", lviv_center);
}

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

const getCoordinates = async () => {
    let coors = await getJSON("/hospitals/" +
        capitalizeFirstLetter(document.getElementById("Info-block__search-form-input").value));
    if (isEmpty(coors)) return [];
    return (Array.isArray(coors) ? coors : [coors]);
};


const reloadMap = async () => {
    let coordinates = await getCoordinates();
    document.getElementsByClassName("Search-form__text")[0].innerHTML =
        "Ми знайшли " + coordinates.length + " точок за вашим запитом.";

    coordinates.map((x) => tomtom.L.marker([x["lon"], x["lat"]]).addTo(map).bindPopup(
         x["name"] + ', ' + x["address"] + ", в навності: " + x["num_present"] + " вакцин"));

    // coordinates.map((x) => tomtom.L.marker([x["lon"], x["lat"]]).addTo(map).bindPopup(x["name"]));
};

