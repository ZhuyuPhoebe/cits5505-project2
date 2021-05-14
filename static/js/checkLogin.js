(function () {
    // Check whether the user is logged in
    var username = localStorage.getItem("username");

    if (username) {
        document.getElementById("user").innerHTML = username;
    } else {
        // Redirect to login page
        window.location.href = 'http://localhost:5000/login';
    }
})();

function logout(event) {
    event.preventDefault();
    localStorage.removeItem('username');
    location.href = 'http://localhost:5000/login';
}
