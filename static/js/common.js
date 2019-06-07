const isEmpty = (obj) => {
    for(let key in obj) {
        if(obj.hasOwnProperty(key))
            return false;
    }
    return true;
};

const getJSON = async (link) => {
    return await fetch(link)
        .then( (response)=>  response.json())
        .then((responseJson)=>{return responseJson});
};

const ConvertToSlash = (date) => {return date.replace('-', '/');};

const ConvertToDMY = (date) => {
    let date_split = date.split("-");
    return date_split[2] + "/" + date_split[1] + "/" + date_split[0];
};

const compareDates = (date1, date2) =>{
    if (date1 > date2){return -1;}
    if (date1 < date2){return 1;}
    return 0;
};


