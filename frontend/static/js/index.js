(function () {
    var username = sessionStorage.getItem("username");
    if (username) {
        $.get('http://localhost:5000/api/units',
        {},
        function(data) {
            if(data.code === 200) {
                var units = data.data;
                var html = '';
                for(var i = 0; i < units.length; i++) {
                    var unit = units[i];
                    var id = unit[0];
                    var title = unit[1];
                    html += "<tr id='" + id + "'><td>" + id + "</td><td>" + title + "</td><td><a class='btn' style='margin:12px;' data-id='"+ id +"' onclick='learn(event)' >Learn</a><a class='btn' style='margin:12px 0;' data-id='"+ id +"' onclick='quiz(event)' >Quiz</a></td></tr>";
                }
                $('#units').append(html);
            }
        });
    }
})();

function learn (e) {
    e.preventDefault();
    var unitId = $(e.target).data('id');
    sessionStorage.setItem("unit", unitId);
    location.href = './learn.html';
}

function quiz (e) {
    e.preventDefault();
    var unitId = $(e.target).data('id');
    sessionStorage.setItem("quiz", unitId);
    location.href = './quiz.html';
}