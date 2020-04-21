Vue.component('course_info', {
    template: `
        <div class="course_info">
            <h2 @click="load">{{course_name}}</h2>
            <p @click="load">{{course_description}}</p>
        </div>`,
    props: {
        course_name:{
            type: "String",
            required: true,
            default: "Course Name"
        },
        course_description:{
            type: "String"
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
            semesters: [
                {
                    name: "Spring 2020",
                    value: "spring20"
                },
                {
                    name:"Fall 2019",
                    value: "fall19"
                },
                {
                    name: "Spring 2019",
                    value: "spring19"
                },
                {
                    name: "Fall 2018",
                    value: "fall18"
                }
            ],
            selected_semester:"Semester",

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

            course_descriptions: [
                {
                    name: "[S20] Probability and Statistics",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "spring20",
                    profile: "math",
                    degree: "bachelor"
                },
                {
                    name: "[F18] Computer Architecture",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "fall18",
                    profile: "cs",
                    degree: "bachelor"
                },
                {
                    name: "[S19] English for Academic Purposes II",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "spring19",
                    profile: "english",
                    degree: "bachelor"
                },
                {
                    name: "[S19] Analytical Geometry and Linear Algebra II",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "spring19",
                    profile: "math",
                    degree: "bachelor"
                },
                {
                    name: "[F19] Operating Systems",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "fall19",
                    profile: "cs",
                    degree: "bachelor"
                },
                {
                    name: "[S20] Control Theory (Linear Control)",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "spring20",
                    profile: "math",
                    degree: "bachelor"
                },
                {
                    name: "[F18] Introduction to Programming I",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "fall18",
                    profile: "cs",
                    degree: "bachelor"
                },
                {
                    name: "[F19] Physics I (mechanics)",
                    desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In nec felis vel leo pellentesque porttitor. Nam a urna eu urna mattis luctus. Nullam dapibus suscipit velit, sed tempor lectus auctor ac. Vivamus sit amet orci at augue rutrum fermentum vitae interdum massa. Praesent in mauris quis sem fringilla consequat. Sed sed neque at sem pharetra volutpat.",
                    semester: "fall19",
                    profile: "math",
                    degree: "bachelor"
                }
            ],
            filter_query: ""
        } 
    },
    computed: {
        filtered_course_descriptions() {
            let res = this.course_descriptions;
            if (this.selected_semester != "Semester"){
                res =  res.filter(course => course.semester === this.selected_semester);
            }
            if(this.selected_profile != "Profile"){
                res =  res.filter(course => course.profile === this.selected_profile);
            }
            if(this.selected_degree != "Degree"){
                res =  res.filter(course => course.degree === this.selected_degree);
            }
            let filter = new RegExp(this.filter_query, "i");
            res = res.filter(course => course.name.match(filter));
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
    }
});
