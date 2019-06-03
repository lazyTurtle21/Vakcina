const ConvertToDMY = (date) => {
    let split_date = date.split('-');
    return new Date(split_date[1] + '/' + split_date[0] + '/' + split_date[2]);
};

const compareDates = (date1, date2) =>{
    if (date1 > date2){return 1;}
    if (date1 < date2){return -1;}
    return 0;
};

const getDoneVaccines = (id) => {
    let vaccines_done = [];
    fetch("/vaccines/done/" + id.toString())
        .then((res) => res.json())
        .then((res) => {vaccines_done = res;});

    let vaccines_age = [];
    fetch("/vaccines/age/")
        .then((res) => res.json())
        .then((res) => {vaccines_age = res;});

    return vaccines_age.filter(x => vaccines_done.find(el => el["id"] === x["id"])["is_done"]);
};

const getDate = (months, birth_date)  => {
    birth_date.setMonth(birth_date.getMonth() + months);
    if (new Date() < birth_date){
        return false;
    }
    return birth_date;
};


const GetOnePost = (data) => {
    let el = document.createElement("div");
    let months = ["Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень", "Серпень", "Вересень",
        "Жовтень", "Листопад", "Грудень"];
    el.innerHTML = `
                  <div class="Year-block__wrapper">
                    <section class="Year-block__content-cell">
                        <h5 class="Year-block__sub-title">${data["vacc_id"]}</h5>
                        <svg class="Year-block__icon" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="16" cy="16" r="16" fill="#CDE6F8" fill-opacity="0.78"/>
<circle cx="16" cy="16" r="15.5" stroke="black" stroke-opacity="0.95"/>
<path d="M22.672 3.82807C22.2447 4.20196 22.2447 4.80828 22.672 5.1824L28.0901 9.92324C28.5174 10.2971 29.2103 10.2971 29.6379 9.92324L31.1859 8.56845L24.22 2.47328L22.672 3.82807Z" fill="#05C46B"/>
<path d="M21.1241 9.2456L24.22 6.53671L26.542 8.56843L23.4461 11.2773L21.1241 9.2456Z" fill="#D1D3D4"/>
<path d="M20.3503 17.3727L12.6105 10.6004L4.87016 17.3727C4.01529 18.1207 4.01529 19.3336 4.87016 20.0816L6.03154 21.0973L7.96629 22.7907L11.0622 25.4996C11.9173 26.2478 13.3034 26.2478 14.1583 25.4996L17.2542 22.7907L21.8981 18.7268L20.3503 17.3727Z" fill="#66BFFF"/>
<path d="M21.1242 9.24559L17.6411 6.19789L12.6105 10.6004L20.3503 17.3727L21.8981 18.7268L26.9292 14.325L21.1242 9.24559Z" fill="#F1F2F2"/>
<path d="M13.2498 25.4991C13.385 25.6172 13.5379 25.7187 13.7041 25.8008C12.8468 26.2366 11.7616 26.1127 11.0607 25.4991L7.96854 22.7886L6.03112 21.0983L4.8708 20.083C4.01727 19.3341 4.01727 18.1217 4.8708 17.3727L12.6095 10.6013L13.7041 11.5591L7.05996 17.3727C6.20642 18.1217 6.20642 19.3341 7.05996 20.083L8.22027 21.0983L10.1577 22.7886L13.2498 25.4991Z" fill="#4E7FFD"/>
<path d="M12.61 10.6011L17.6395 6.2L18.7341 7.15775L13.7043 11.5588L12.61 10.6011Z" fill="#E6E7E8"/>
<path d="M4.48326 22.4521C4.05596 22.826 4.05596 23.4323 4.48326 23.8062L5.64464 24.822L6.41854 25.4996L6.80549 25.8382C7.23306 26.2121 7.92572 26.2121 8.35329 25.8382L9.90163 24.4834L7.96634 22.7907L6.03159 21.0974L4.48326 22.4521Z" fill="#05C46B"/>
<path d="M4.87021 24.1448L1.82913 26.8065C0.823805 27.6859 0.369246 28.9376 0.609753 30.1635L0.680302 30.521L6.41855 25.4996L5.64465 24.822L4.87021 24.1448Z" fill="#D1D3D4"/>
<path d="M31.5724 8.22985L24.607 2.13468C24.39 1.95511 24.0504 1.95511 23.8331 2.13468L22.2856 3.48901C21.6443 4.04996 21.6443 4.95978 22.2856 5.52096L23.4465 6.53647L21.1242 8.56843L18.0281 5.85955C17.8146 5.67248 17.468 5.67248 17.2542 5.85955L4.48323 17.0341C3.41645 17.9697 3.41645 19.4844 4.48323 20.4202L5.25767 21.0973L4.09628 22.1136C3.4552 22.6745 3.4552 23.5843 4.09628 24.1453L1.44268 26.4679C0.312564 27.4579 -0.198649 28.8658 0.0704528 30.2449L0.141269 30.6026C0.175742 30.7787 0.319779 30.9232 0.514323 30.9775C0.709401 31.0317 0.922651 30.9863 1.06722 30.8596L6.41852 26.1768C7.05987 26.7379 8.0994 26.7379 8.74075 26.1768L9.9016 25.1605L10.6752 25.8382C11.7447 26.7716 13.4758 26.7716 14.5453 25.8382L22.2851 19.0659L27.3157 14.6636C27.5292 14.4765 27.5292 14.1735 27.3157 13.9864L24.2196 11.2775L26.5413 9.24559L27.7026 10.2618C28.3437 10.8225 29.383 10.8225 30.0241 10.2618L31.5719 8.90701C31.7857 8.72018 31.7859 8.41691 31.5724 8.22985V8.22985ZM1.09448 29.481C1.10517 28.6039 1.50789 27.7651 2.21658 27.1446L4.87018 24.822L5.64408 25.4996L1.09448 29.481ZM7.96685 25.4991C7.75013 25.6803 7.40914 25.6803 7.19242 25.4991L4.87018 23.4672C4.76757 23.3774 4.70984 23.2556 4.70984 23.1284C4.70984 23.0014 4.76757 22.8796 4.87018 22.7898L6.03103 21.774L9.12717 24.4829L7.96685 25.4991ZM24.2214 16.0175L23.0595 15.0022C22.9219 14.8778 22.7185 14.8277 22.5272 14.8715C22.3358 14.9154 22.1865 15.0461 22.1362 15.2136C22.0863 15.381 22.1432 15.5592 22.2856 15.6793L23.4465 16.6955L21.8981 18.0501L20.7373 17.0341C20.5235 16.8468 20.1769 16.8468 19.9631 17.0339C19.7493 17.2207 19.7491 17.524 19.9628 17.7111L21.1242 18.7273L19.5764 20.0816L18.415 19.0659C18.2005 18.8844 17.8589 18.887 17.6478 19.0717C17.4367 19.2564 17.4338 19.5553 17.6411 19.743L18.8025 20.7588L17.2542 22.1136L16.0931 21.0973C15.8782 20.9159 15.537 20.9185 15.3259 21.1032C15.1147 21.2879 15.1118 21.5865 15.3192 21.7745L16.4806 22.7907L14.9322 24.1448L13.7714 23.1293C13.634 23.0047 13.4304 22.9549 13.239 22.9986C13.0477 23.0423 12.8983 23.1733 12.8484 23.3407C12.7981 23.5081 12.8553 23.686 12.9975 23.8062L14.1583 24.822L13.7714 25.161C13.1295 25.7208 12.091 25.7208 11.4491 25.161L5.25713 19.743C4.61738 19.1814 4.61738 18.2727 5.25713 17.7111L12.6105 11.2775L18.415 16.3565C18.6299 16.5379 18.9711 16.5354 19.1823 16.3507C19.3934 16.1659 19.3963 15.8671 19.1889 15.6793L13.3844 10.6004L17.6411 6.87552L26.1554 14.325L24.2214 16.0175ZM23.4465 10.6004L21.8981 9.24559L24.2201 7.2141L25.7679 8.56843L23.4465 10.6004ZM29.251 9.58417C29.0372 9.771 28.6909 9.771 28.4771 9.58417L23.059 4.84333C22.8455 4.65627 22.8455 4.35347 23.059 4.16664L24.2201 3.14996L30.4129 8.56843L29.251 9.58417Z" fill="#231F20"/>
</svg>
                        <p class="Year-block__sub-text">${months[data["age"].getMonth()]}, ${data["age"].getUTCFullYear()}</p>
                    </section>
                </div>
    `;
    return el;
};


const GetFullPost = async (year, data) => {
    let el = document.createElement("article");
    el.className = "Year-block Main-block__year-block";
    el.id = "Year-" + year.toString();
    el.innerHTML = `
            <div class="Year-block__year">
                <span>${year}</span>
                <img src="../static/images/vaccine.svg" class="Year-block__small-icon" alt="syringe">
            </div>
    `;

    document.querySelector(".Main-block").appendChild(el);

    console.log(year);

    const historyContainer = document.querySelector("#Year-" + year);
    data.map(post_data => historyContainer.appendChild(GetOnePost(post_data)));

};



const initHistory = () => {
    // let client_birth = client["date_of_birth"];
    let client = {};
    let id = 1;
    fetch("/clients/" + id.toString())
        .then((res) => res.json())
        .then((res) => {client = res;});

    if (client.length === 0){

    }

    let client_birth = "";
    let client_id = 1;

    let vaccines = getDoneVaccines(client_id);
    vaccines.map(x => {x["age"] = getDate(x["age"], ConvertToDMY(client_birth))});
    vaccines = vaccines.filter(x => x["age"]);
    vaccines.sort((x, y) => {return compareDates(x["age"], y["age"]);});

    let today = new Date();
    let current_year_events = vaccines.filter(x => {return x["age"].getFullYear() === today.getFullYear();});
    let other_years_events = vaccines.filter(x => {return x["age"].getFullYear() !== today.getFullYear();});

    if (current_year_events.length !== 0){
        GetFullPost(today.getFullYear(), current_year_events);
    }

    if (other_years_events.length !== 0){
        let first_event = other_years_events[other_years_events.length - 1]["age"].getFullYear().toString();
        let last_event = other_years_events[0]["age"].getFullYear().toString();
        if (first_event === last_event){
            GetFullPost(first_event, other_years_events);
        } else{
            GetFullPost(last_event + '-' + first_event, other_years_events);
        }
    }
    // console.log(vaccines);
    if (other_years_events.length === 0 && current_year_events.length === 0){
        GetFullPost(today.getFullYear(), [{"vacc_id": "У вас ще немає зроблених вакцин.", "age":today}]);
    }


    // vaccines_age.map((x) => {x["age"] = getDate(x["age"], ConvertToDMY(client_birth))});
    // vaccines_age = vaccines_age.filter(x => x["age"]);
    // vaccines_age.sort((x, y) => {return compareDates(x["age"], y["age"]);});

};


initHistory();