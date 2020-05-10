Vue.component('course_info', {
    template: `
        <div class="course_info">
            <h2 @click="load">{{course_name}}</h2>
        </div>`,
    props: {
        course_name:{
            type: "String",
            required: true,
            default: "Course Name"
        }
    },
    methods: {
        load(){
            window.location.href = "https://www.youtube.com/watch?v=dQw4w9WgXcQ";
        }
    }
})


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
            console.log(this.courses);
        })
    }
});
