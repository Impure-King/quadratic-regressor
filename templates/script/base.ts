const button_toggler = document.getElementById("toggler");

var toggle = 0;

button_toggler?.addEventListener('click', () => {
    if (toggle % 2 == 0){
        alert("The navbar was toggled");
        alert("lol")
    }
    toggle += 1;
});