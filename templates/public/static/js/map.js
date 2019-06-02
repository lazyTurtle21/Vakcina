let map = tomtom.L.map('map', {
    key: 'Jvod0PUA0hjxGkT1AwIWJVdeGeV5pkr0',
    basePath: 'sdk',
    center: [49.840838, 24.028037],
    zoom: 13
});


const initMap = () => {
    let coordinates = [];
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState === 4 && this.status === 200) {
            coordinates = JSON.parse(this.responseText);
        }
    };
    xhttp.open("GET", "https://localhost:5000/hospitals/" +
        document.getElementById("Info-block__search-form"), true);
    xhttp.send();
    document.getElementsByClassName("Search-form__text")[0].innerHTML = "Ми знайшли " + coordinates.length +
        " точок за вашим запитом.";

    coordinates.map((x) => tomtom.L.marker([x["long"], x["lat"]]).addTo(map).bindPopup(x["name"]));
};


// initMap([
//     {"name": "hosp1", "long": 49.840838, "lat": 24.028037},
//     {"name": "hosp2", "long": 49.85, "lat": 24.058037}
// ]);
