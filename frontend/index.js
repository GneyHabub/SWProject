let flag = false;

document.getElementById("switch").addEventListener("click", function () {
    if (!flag) {
        document.getElementById("poll_id").style.display = "inline";
        document.getElementById("switch").innerText = "Login as a staff member";
        document.getElementById("access_header_text").innerText = "Student Access";
        flag = true;
    }else {
        document.getElementById("poll_id").style.display = "none";
        document.getElementById("switch").innerText = "Login as a student";
        document.getElementById("access_header_text").innerText = "University Staff Access";
        flag = false;
    }

});
