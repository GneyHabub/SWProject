const course_name = "Probability and Statistics"
let data = {
    "fall16": [],
    "spring17": [],
    "fall17": [],
    "spring18":[],
    "fall18":[],
    "spring19":[],
    "fall19":[],
    "spring20":[]
};
for (let item in data){
    for (let i = 0; i < 80; i++){
        data[item].push(Math.floor(40 + Math.random()*60))
    }
}
