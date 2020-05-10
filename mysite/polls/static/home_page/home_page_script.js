Vue.component('rank_item', {
    template: `
        <div>
            <h3>{{ prof_name }}</h3>
        </div>`,
    props: {
        prof_name:{
            type: "String",
            required: true,
            default: "Name Error Happened"
        }
    }
});

Vue.component('profs_place', {
    template: `
        <div class="profs_place_wrapper">
            <h1> Your position is: </h1>
            <h1 class="profs_place_content">{{ place }}</h1>
        </div>`,
    props: {
        place:{
            type: Number
        }
    }
});

new Vue({
    el: "#app",
    data: function() {
        return {
            profs_top: {
                type: Array
            },
            top_length: {
                type: Number
            },
            place: {
                type: Number
            }
        }
    },
    computed: {
    },
    methods: {
    },
    created() {
        const url = window.location.href.slice(0, -4) + "ranking/";
        fetch(url).then(res => {
            return res.json();
        }).then(res => {
            this.profs_top = res["TOP"];
            this.place = res["PLACE"];
            this.top_length = this.profs_top.length;
            for (let i =0; i<this.profs_top.length; i++){
                console.log(this.profs_top[i].name);
            }
        })
    }
});

// var ctx = document.getElementById('myChart').getContext('2d');
// var myChart = new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ['1', '2', '3', '4', '5', '6'],
//         datasets: [{
//             label: '# of Votes',
//             data: [1, 2, 4, 8, 16, 32],
//             backgroundColor: [
//                 'rgba(255,28,31,0.35)'
//             ],
//             borderColor: [
//                 'rgb(246,14,34)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         lineTension: 0.1,
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });
// var ctx1 = document.getElementById('myChart1').getContext('2d');
// var myChart1 = new Chart(ctx1 , {
//     type: 'line',
//     data: {
//         labels: ['1', '2', '3', '4', '5', '6', '7'],
//         datasets: [{
//             label: '# of Votes',
//             data: [16, 4, 2, 1, 2, 4, 16],
//             backgroundColor: [
//                 'rgba(82,73,255,0.35)'
//             ],
//             borderColor: [
//                 'rgb(3,0,246)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         lineTension: 0.1,
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });