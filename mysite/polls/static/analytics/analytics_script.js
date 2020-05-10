let total_data = [];
let total_labels = [];
let years = [];
let main_colors = [
    'rgba(78, 169, 32, 0.35)',
    'rgba(182, 34, 63, 0.35)',
    'rgba(37, 59, 132, 0.35)',
    'rgba(195,146, 37, 0.35)'
];

window.onload = () => {
    const url = window.location.href.slice(0, -1) + "_api/";
    console.log(url);
    fetch(url).then(res => {
        return res.json();
    }).then(res => {
        res["COURSE_GRADE"].forEach(item => {
            total_labels.push(item["NAME"]);
            total_data.push(item["AV_GRADE"]);
        });
        res["YEAR_GRADE"].forEach(item => {
            if(!(years.find(year => year === item["YEAR"]))) {
                years.push(item["YEAR"]);
            }
        });

        let current_colors = [];
        for (let i =0; i < total_labels.length; i++){
            current_colors.push(main_colors[i%4])
        }

        let datasets = [];
        for (let i = 0; i < total_labels.length; i++){
            datasets.push({
                label: total_labels[i],
                data: [],
                borderColor: current_colors[i],
                borderWidth: 4,
                fill: 'none'
            })
        }
        years.forEach(year => {
            let year_grade_filtered = res["YEAR_GRADE"].filter(item => item["YEAR"] === year);
            datasets.forEach(dataset => {
                let data_item = year_grade_filtered.find(item => dataset.label === item["RES"]["NAME"]);
                if (data_item) {
                    dataset.data.push(data_item["RES"]["AV_GRADE"]);
                } else {
                    dataset.data.push(null);
                }
            })
        });

        let ctx1 = document.getElementById('chart1').getContext('2d');
        let myChart1 = new Chart(ctx1, {
            type: 'bar',
            data: {
                labels: total_labels,
                datasets: [{
                    label: 'Average result',
                    data: total_data,
                    backgroundColor: current_colors,
                    borderWidth: 1
                }]
            },
            options: {
                lineTension: 0,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });

        let ctx2 = document.getElementById('chart2').getContext('2d');
        let myChart2 = new Chart(ctx2, {
            type: 'line',
            data: {
                labels: years,
                datasets: datasets
            },
            options: {
                lineTension: 0,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });
    })
};
// document.getElementsByClassName("page_title")[0].innerHTML = course_name;