let login_switch_flag = false;

document.getElementById("switch").addEventListener("click", function () {
    if (!login_switch_flag) {
        document.getElementById("survey_id").style.display = "inline";
        document.getElementById("switch").innerText = "Login as a staff member";
        document.getElementById("access_header_text").innerText = "Student Access";
        login_switch_flag = true;
    }else {
        document.getElementById("survey_id").style.display = "none";
        document.getElementById("switch").innerText = "Login as a student";
        document.getElementById("access_header_text").innerText = "University Staff Access";
        login_switch_flag = false;
    }

});
