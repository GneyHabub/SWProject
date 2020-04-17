Vue.component('course_info', {
    template: `
        <div class="course_info">
            <h2>{{course_name}}</h2>
            <p>{{course_description}}</p>
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
                    name: "Math",
                    desc: "ouygugv",
                    semester: "spring20",
                    profile: "math",
                    degree: "bachelor"
                },
                {
                    name: "CompArc",
                    desc: "jgvugvvo",
                    semester: "spring19",
                    profile: "cs",
                    degree: "bachelor"
                },
                {
                    name: "English",
                    desc: "jgvugvvo",
                    semester: "fall19",
                    profile: "english",
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
    }
});
