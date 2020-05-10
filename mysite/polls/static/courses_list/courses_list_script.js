Vue.component('course_info', {
    template: `
        <div class="course_info">
            <a :href="analytics_url">{{course_info.NAME}}</a>
        </div>`,
    data() {
        return {
            analytics_url: {
                type: String
            }
        }
    },
    props: {
        course_info:{
            type: Object,
            required: true
        }
    },
    created() {
        this.analytics_url = window.location.href.slice(0, -8) + this.course_info["ID"] + "/single_course/"
    },
    methods: {
        load(){
            window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
        }
    }
});


new Vue({
    el: "#app",
    data: function(){ 
        return{
            courses: [],
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
            let res = this.courses;
            let filter = new RegExp(this.filter_query, "i");
            res = res.filter(course => course["NAME"].match(filter));
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
            this.courses = res["COURSES"];
        })
    }
});
