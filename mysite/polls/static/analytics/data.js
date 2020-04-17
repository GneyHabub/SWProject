let data = {
    "spring_2018":[],
    "fall_2018":[],
    "spring_2019":[],
    "fall_2019":[],
    "spring_2020":[]
};
for (let item in data){
    for (let i = 0; i < 80; i++){
        data[item].push(Math.floor(40 + Math.random()*60))
    }
    console.log(data[item].reduce( ( p, c ) => p + c, 0 )/data[item].length);
}
