const getDoneVaccines = (id) => {
    let vaccines_done = [{"vacc_id" : 1, "is_done" : true}, {"vacc_id" : 2, "is_done" : true}];
    // let vaccines_age = getVaccinesDates();  [{"name" : "vacc_name1", age: 2}, {""name" : "vacc_name2", age: 72}]
    let vaccines_age = [{"vacc_id" : 1, "age": 200}, {"vacc_id" : 2, "age": 228}];
    vaccines_age = vaccines_age.filter(x => vaccines_done.find(el => el["vacc_id"] === x["vacc_id"])["is_done"]);
    return vaccines_age;
};




const initHistory = () => {
    // let client_birth = client["date_of_birth"];
    let client_birth = "28-03-2000";
    let client_id = 1;
    // let vaccines_done = getVaccinesDone(1);
    // let vaccines_done = [{"vacc_id" : 1, "is_done" : false}, {"vacc_id" : 2, "is_done" : false}];
    // let vaccines_age = getVaccinesDates();  [{"name" : "vacc_name1", age: 2}, {""name" : "vacc_name2", age: 72}]
    // let vaccines_age = [{"vacc_id" : 1, "age": 312}, {"vacc_id" : 2, "age": 231}];

    let vaccines = getDoneVaccines(client_id);


    vaccines_age.map((x) => {x["age"] = getDate(x["age"], ConvertToDMY(client_birth))});
    vaccines_age = vaccines_age.filter(x => x["age"]);
    vaccines_age.sort((x, y) => {return compareDates(x["age"], y["age"]);});

};