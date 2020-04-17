new Vue({
    el:"#app",
    data() {
        return {
            
        }
    }
});

let avg_data = [];
for (let item in data){
    avg_data.push(data[item].reduce( ( p, c ) => p + c, 0 )/data[item].length);
}

var ctx = document.getElementById('myChart').getContext('2d');
                var myChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: Object.keys(data),
                        datasets: [{
                            label: '# of Votes',
                            data: avg_data,
                            backgroundColor: [
                                'rgba(255,28,31,0.35)'
                            ],
                            borderColor: [
                                'rgb(246,14,34)'
                            ],
                            borderWidth: 1
                        }]
                    },
                    options: {
                        lineTension: 0.1,
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true
                                }
                            }]
                        }
                    }
                });