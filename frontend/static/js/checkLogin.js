(function () {
    var username = sessionStorage.getItem("username");
    if (username) {
        document.getElementById("user").innerHTML = username;
    } else {
        window.location.href = './login.html';
    }
})();