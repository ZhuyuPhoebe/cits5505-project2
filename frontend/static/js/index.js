function renderUnits(units) {
    var html = '';
    for (var i = 0; i < units.length; i++) {
        var unit = units[i];
        var id = unit[0];
        var title = unit[1];
        html += "<tr id='" + id + "'>";
        html += "<td>" + id + "</td>";
        html += "<td>" + title + "</td>";
        html += "<td>";
        // Learn button
        html += "<a class='btn' style='margin: 12px;' data-id='" + id + "' onclick='learn(event)' >Learn</a>";
        // Quiz button
        html += "<a class='btn' style='margin:12px 0;' data-id='" + id + "' onclick='quiz(event)' >Quiz</a>";
        html += "</td>";
        html += "</tr>";
    }
    return html;
}

(function () {
    var username = localStorage.getItem("username");
    if (username) {
        // get units
        $.get('http://localhost:5000/api/units',
            {},
            function (data) {
                if (data.code === 200) {
                    var units = data.data;
                    var html = renderUnits(units);
                    // append to DOM
                    $('#units').append(html);
                }
            });
    }
})();

function learn(e) {
    // Redirect to learning page
    e.preventDefault();
    var unitId = $(e.target).data('id');
    // Storage unit id
    localStorage.setItem("unit", unitId);
    location.href = './learn.html';
}

function quiz(e) {
    // Redirect to quiz page
    e.preventDefault();
    var unitId = $(e.target).data('id');
    // Storage quiz id
    localStorage.setItem("quiz", unitId);
    location.href = './quiz.html';
}
