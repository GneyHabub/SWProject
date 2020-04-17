let avg_data = [];
for (let item in data){
    avg_data.push(data[item].reduce( ( p, c ) => p + c, 0 )/data[item].length);
}

document.getElementsByClassName("page_title")[0].innerHTML = course_name;

let ctx = document.getElementById('chart').getContext('2d');
                let myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: Object.keys(data),
                        datasets: [{
                            label: 'Average result',
                            data: avg_data,
                            backgroundColor: [
                                'rgba(78, 169, 32, 0.35)'
                            ],
                            borderColor: [
                                'rgb(120, 169, 78)'
                            ],
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