// Ensuring the DOM content has loaded
function validateNonEmpty2() {
    var x1 = document.forms['solver_2']["x1"].value;
    var y1 = document.forms["solver_2"]["y1"].value;
    var x2 = document.forms['solver_2']["x2"].value;
    var y2 = document.forms["solver_2"]["y2"].value;
    var x3 = document.forms['solver_2']["x3"].value;
    var y3 = document.forms["solver_2"]["y3"].value;
    
    if (x1 == "" || x2 == "" || x3 == "" || y1 == "" || y2 == "" || y3 == "") {
        alert("One of the coordinates have not been filled out.");
        return false;
    }
    obj = document.getElementById("solver_1");
    obj.style.display = "none";

}

function validateNonEmpty1() {
    var vertexx = document.forms['solver_1']["vertexx"].value;
    var vertexy = document.forms["solver_1"]["vertexy"].value;
    var pointx = document.forms['solver_1']["pointx"].value;
    var pointy = document.forms["solver_1"]["pointy"].value;

    if (vertexx == "" || vertexy == "" || pointx == "" || pointy == "") {
        alert("One of the coordinates have not been filled out.");
        return false;
    }
    else{
        if (parseFloat(vertexy) == parseFloat(pointy) && parseFloat(pointx) == parseFloat(vertexx)) {
            alert("These are coincidental points.");
            return false;
        }
        if (parseFloat(vertexx) == parseFloat(pointx)) {
            alert("The vertex and the point can't have the same x-coordinate."); // Add explaination.
            return false;
        }
        if (parseFloat(vertexy) == parseFloat(pointy)) {
            alert("The vertex and the point can't have the same y-coordinate.");
            return false;
        }
    }

}

function changeForm() {
    var method_name = document.getElementById("methods").value;
    const method1 = document.getElementById("solver_1");
    const method2 = document.getElementById("solver_2");
    method1.style.display = "none";
    method2.style.display = "none";
    if (parseInt(method_name) === 1) {
        method1.style.display = "block";
    }
    else if (parseInt(method_name) === 2) {
        method2.style.display = "block";
    }
}