// Ensuring the DOM content has loaded


function vertexEquationConcatenator(a, h, k) {

    // Looping through and checking if any argument is an int:
    if (a == parseInt(a)) {
        a = parseInt(a);
    }

    if (h == parseInt(h)) {
        h = parseInt(h);
    }

    if (k == parseInt(k)) {
        k = parseInt(k);
    }

    let a1 = a;
    let h1 = h;
    let k1 = k;
    if (a.toString().match('e') != null){
        a1 = a.toString().split('e')[0] + " * 10^{" + a.toString().split('e')[1] + "}"
    }
    if (h.toString().match('e') != null){
        h1 = h.toString().split('e')[0] + " * 10^{" + h.toString().split('e')[1] + "}"
    }
    if (k.toString().match('e') != null){
        k1 = k.toString().split('e')[0] + " * 10^{" + k.toString().split('e')[1] + "}"
    }

    // Starting string concatenation:
    let part1 = `y = `;
    let part2 = `(x - ${h})^2`;
    let part3 = ` + ${k}`;

    // Checking various special cases.
    if (h == 0){
        part2 = "x^2";
    }
    else if (h < 0){
        part2 = `(x + ${Math.abs(h)})^2`;
    }
    
    if (a == 0){
        part2 = "";
    }
    else if (a != 1){
        part2 = `${a}` + part2;
    }

    if (k == 0){
        part3 = "";
    }
    else if (k < 0){
        part3 = ` - ${Math.abs(k)}`;
    }
    
    const equation = part1 + part2 + part3;
    return [equation, `y = ${a1}(x - ${h1})^2 + ${k1}`];
}

function leadingCoefficientSolver(h, k, x, y) {
    return (y - k)/(x - h)**2;
}

function validateNonEmpty1() {
    // Receiving values:
    var vertexx = document.forms['solver_1']["vertexx"].value;
    var vertexy = document.forms["solver_1"]["vertexy"].value;
    var pointx = document.forms['solver_1']["pointx"].value;
    var pointy = document.forms["solver_1"]["pointy"].value;

    // Alerting if the values were not filled out:
    if (vertexx == "" || vertexy == "" || pointx == "" || pointy == "") {
        alert("One of the coordinates have not been filled out.");
        return false;
    }
    else{
        // Checking other illegal cases:
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

    // Getting the answer:
    var h = parseFloat(vertexx);
    var k = parseFloat(vertexy);
    var x = parseFloat(pointx);
    var y = parseFloat(pointy);

    var a = leadingCoefficientSolver(h, k, x, y);

    // Returning the general equation:
    var [equation, equation1] = vertexEquationConcatenator(a, h, k);

    // Writing the equation:
    const answer = document.getElementById("answer");
    answer.textContent = equation;
    const answerBox = document.getElementById("answerBox");
    answerBox.style.display = "block";
    const calcBox = document.getElementById("calculatorBox");
    calcBox.style.display = "flex";

    if (id >= 100){
        alert("Too many graph sessions. Please reload to try again.")   
    }
    else {
        calculator?.setExpression({id:`graph${id}`, latex:equation1});
        id += 1;
    }
    return false

}

function generalCoefficientSolver(x1, x2, x3, y1, y2, y3) {
    // Calculating the a coefficient:
    let a = ((y1-y3)*(x2-x3) - (y2-y3)*(x1-x3))/((x1-x2)*(x2-x3)*(x1-x3));
    
    // Calculating the b coefficient;
    let b = ((y1 - y3) - (x1**2 - x3**2) * a)/(x1 - x3);

    // Calculating the c coefficient:
    let c = y1 - a*x1**2  - b*x1;
    return [a, b, c];
}

function generalEquationConcatenator(a, b, c){
    // Checking if any coefficient is an integer:
    if (a == parseInt(a)) {
        a = parseInt(a);
    }
    if (b == parseInt(b)) {
        b = parseInt(b);
    }
    if (c == parseInt(c)) {
        c = parseInt(c);
    }
    let a1 = a;
    let b1 = b;
    let c1 = c;
    if (a.toString().match('e') != null){
        a1 = a.toString().split('e')[0] + " * 10^{" + a.toString().split('e')[1] + "}"
    }
    if (b.toString().match('e') != null){
        b1 = b.toString().split('e')[0] + " * 10^{" + b.toString().split('e')[1] + "}"
    }
    if (c.toString().match('e') != null){
        c1 = c.toString().split('e')[0] + " * 10^{" + c.toString().split('e')[1] + "}"
    }
    
    part0 = "y = ";
    part1 = `${a}x^2`;
    part2 = ` + ${b}x`;
    part3 = ` + ${c}`;

    // Testing out special cases:
    if (a == 1) {
        part1 = "x^2";
    }
    else if (a == 0){
        part1 = "";
    }

    if (b == 0) {
        part2 = "";
    }
    else if (b < 0) {
        part2 = ` - ${Math.abs(b)}x`;
    }
    else if (a==0 && b>0) {
        part2 = `${b}x`
    }

    if (a==0 && b==0 && c >= 0) {
        part3 = `${c}`
    }
    else if (c == 0) {
        part3 = "";
    }
    else if (c < 0) {
        part3 = ` - ${Math.abs(c)}`;
    }

    return [part0 + part1 + part2 + part3, `y = ${a1}x^2 + ${b1}x + ${c1}`];
}

function validateNonEmpty2() {
    // Receiving values:
    var x1 = document.forms['solver_2']["x1"].value;
    var y1 = document.forms["solver_2"]["y1"].value;
    var x2 = document.forms['solver_2']["x2"].value;
    var y2 = document.forms["solver_2"]["y2"].value;
    var x3 = document.forms['solver_2']["x3"].value;
    var y3 = document.forms["solver_2"]["y3"].value;
    
    // Alerting if any of the values were not filled out:
    if (x1 == "" || x2 == "" || x3 == "" || y1 == "" || y2 == "" || y3 == "") {
        alert("One of the coordinates have not been filled out.");
        return false;
    }

    var x1 = parseFloat(x1);
    var y1 = parseFloat(y1);
    var x2 = parseFloat(x2);
    var y2 = parseFloat(y2);
    var x3 = parseFloat(x3);
    var y3 = parseFloat(y3);

    // Optional Handling of Coincidental points:
    let list1 = [x1, y1];
    let list2 = [x2, y2];
    let list3 = [x3, y3];
    if (list1[0] == list2[0] && list1[1] == list2[1] || list2[0] == list3[0] && list2[1] == list3[1] || list1[0] == list3[0] && list1[1] == list3[1]){
        alert(" 2 or more coincident coordinates have been given.");
        return false;
    }

    // Same x case handling:
    if (list1[0] == list2[0] || list2[0] == list3[0] || list1[0] == list3[0]){
        alert("2 or more points can't have the same x-coordinate, since we are graphing a function.");
        return false;
    }

    // Getting the appropriate values:
    const arrayOfCoefficients = generalCoefficientSolver(x1, x2, x3, y1, y2, y3);

    let [a, b, c] = arrayOfCoefficients;
    var [equation, equation1] = generalEquationConcatenator(a, b, c);

    // Displaying the answer:
    var answerBox = document.getElementById("answerBox");
    var answer = document.getElementById("answer");
    answer.textContent = equation;
    answerBox.style.display = "block";
    const calcBox = document.getElementById("calculatorBox");
    calcBox.style.display = "flex";

    // Graphing the answer:
    if (id >= 100){
     alert("Too many graph sessions. Please clear some on desmos.")   
    }
    else {
        calculator?.setExpression({id:`graph${id}`, latex:equation1});
        id += 1;
    }
    return false;
}


// Helpful function for changing the divs:
function changeForm() {
    var method_name = document.getElementById("methods").value;
    const method1 = document.getElementById("solver_1");
    const method2 = document.getElementById("solver_2");
    const exp1 = document.getElementById("explaination1");
    const exp2 = document.getElementById("explaination2");
    method1.style.display = "none";
    method2.style.display = "none";
    exp1.style.display = "none";
    exp2.style.display = "none";
    if (parseInt(method_name) === 1) {
        method1.style.display = "block";
        exp1.style.display = "block";
    }
    else if (parseInt(method_name) === 2) {
        method2.style.display = "block";
        exp2.style.display = "block";
    }
}
