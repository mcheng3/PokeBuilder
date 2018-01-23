var del = document.getElementById("del");
console.log(del)

var warning = function(e) {
    alert("Your team will be permanently deleted.")
};

del.addEventListener("click", warning);
