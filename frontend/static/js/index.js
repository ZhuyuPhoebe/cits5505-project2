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
        html += "<a class='btn btn2' style='margin:12px 0;' data-id='" + id + "' onclick='quiz(event)' >Quiz</a>";
        html += "</td>";
        html += "</tr>";
    }
    return html;
}

(function () {
    banner();//banner
    // learnfn();
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
// banner
function banner() {
    var $banner = $("#wrap"),
        $pic = $("#pic"),
        $list =$("#list li"),
        index = 0,
        timer = null;
    // clear time
    if (timer) {
        clearInterval(timer);
        timer = null;
    }
    // auto
    timer = setInterval(autoPlay, 2000);    
    function autoPlay() {
        index++;
        if (index >= $list.length) {
            index = 0;
        }
        changeImg(index);
    }
    // changer
    function changeImg(curIndex) {
        for (var j = 0; j < $list.length; j++) {
            $list[j].className = "";
        }
        $list[curIndex].className = "on";
        $pic[0].style.marginTop = -500 * curIndex + "px";
        index = curIndex;
    }
    // stop
    $banner.onmouseover = function() {
        clearInterval(timer);
    }
    // nest
    $banner.onmouseout = function() {
        timer = setInterval(autoPlay, 2000);
    }
    // 
    for (var i = 0; i < $list.length; i++) {
        $list[i].id = i;
        $list[i].onmouseover = function() {
            clearInterval(timer);
            changeImg(this.id);
        }
    }
}
