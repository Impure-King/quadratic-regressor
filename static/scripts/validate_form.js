// Ensuring the DOM content has loaded
function validateNonEmpty() {
    var vertexx = document.forms['solver_1']["vertexx"].value;
    var vertexy = document.forms["solver_1"]["vertexy"].value;
    var pointx = document.forms['solver_1']["pointx"].value;
    var pointy = document.forms["solver_1"]["pointy"].value;

    if (vertexx == "" || vertexy == "" || pointx == "" || pointy == "") {
        alert("One of the points have not been filled out.");
        return false;
    }

    else if (parseFloat(vertexx) == parseFloat(pointx)) {
        alert("The vertex and the point can't have the same x-coordinate.");
        return false;
    }

}