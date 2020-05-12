Vue.component('survey_info', {
    template: `
        <div class="survey_info">
            <h2 >{{survey.poll_title}}</h2>
            <a :href="csv_link">
                <button>Download results in CSV</button>
            </a>
            <div class="date_semester_wrapper">
                <p>{{semester}}</p>
                <p>{{survey.year}}</p>
            </div>
        </div>`,
    data() {
        return {
            semester: {
                type: "String"
            },
            csv_link: {
                type: "String"
            }
        }
    },
    props: {
        survey:{
            type: Object,
            required: true
        }
    },
    created() {
        this.semester = this.survey.semester ? 'Fall' : 'Spring';
        this.csv_link = "/polls/" + this.survey.poll_id + "/poll_export/"
    }
});


new Vue({
    el: "#app",
    data: function(){
        return{
            surveys: [],
            profiles: [
                {
                    name: "Math",
                    value: "math"
                },
                {
                    name: "Computer Science",
                    value: "cs"
                },
                {
                    name: "English",
                    value: "english"
                }
            ],
            selected_profile: "Profile",

            degrees: [
                {
                    name: "Bachelor",
                    value: "bachelor"
                },
                {
                    name: "Master",
                    value: "master"
                }
            ],
            selected_degree: "Degree",
            filter_query: ""
        }
    },
    computed: {
        filtered_course_descriptions() {
            let res = this.surveys;
            let filter = new RegExp(this.filter_query, "i");
            res = res.filter(survey => survey.poll_title.match(filter));
            return res;
        }
    },
    methods: {
        reset_filter() {
            this.selected_semester = "Semester";
            this.selected_profile = "Profile";
            this.selected_degree = "Degree";
            this.filter_query = "";
        }
    },
    created() {
        const url = window.location.href.slice(0, -1) + "_api/";
        fetch(url).then(res => {
            return res.json();
        }).then(res => {
            this.surveys = res["SURVEYS"];
            console.log(res);
        })
    }
});