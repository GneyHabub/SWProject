let data = [];
let labels = [];
let main_colors = [
    'rgba(78, 169, 32, 0.35)',
    'rgba(182, 34, 63, 0.35)',
    'rgba(37, 59, 132, 0.35)',
    'rgba(195,146, 37, 0.35)'
];

window.onload = () => {
    const url = window.location.href.slice(0, -14) + "subject_analytics/";
    fetch(url).then(res => {
        return res.json();
    }).then(res => {
        document.getElementsByClassName("page_title")[0].innerHTML = res["NAME"];
        res["RESULTS"].forEach(item => {
            labels.push(new Date(item["DATE"]).toDateString());
            data.push(item["GRADE"]);
        });
        let ctx1 = document.getElementById('chart1').getContext('2d');
        let myChart1 = new Chart(ctx1, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Average Result For Each Poll',
                    data: data,
                    borderColor: '#8b21ff',
                    borderWidth: 4,
                    fill: 'none',
                    lineTension: 0
                }]
            },
            options: {
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