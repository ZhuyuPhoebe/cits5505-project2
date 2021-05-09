function renderNav(sections) {
    var nav = '';
    for (var i = 0; i < sections.length; i++) {
        var section = sections[i];
        var id = section[0];
        var title = section[1];
        nav += "<a href='#" + id + "' class='list-group-item list-group-item-success'>" + title + "</a>";
    }
    // Append to DOM
    $('#left-nav').append(nav);
}

function renderContent(sections) {
    var html = '<div>';
    for (var i = 0; i < sections.length; i++) {
        var section = sections[i];
        var id = section[0];
        var title = section[1];
        var detail = section[2];
        html += "<h4 id='" + id + "'>" + title + "</h4>";
        html += "<p>" + detail + "</p><hr />";
    }
    html += '</div>';
    // Append to DOM
    $('#learn').append(html);
}

(function () {
    var username = localStorage.getItem("username");
    var chapterId = localStorage.getItem("chapter");
    if (username && chapterId) {
        // get sections
        $.get('http://localhost:5000/api/sections',
            {
                id: chapterId
            },
            function (data) {
                if (data.code === 200) {
                    var sections = data.data;
                    renderContent(sections);
                    renderNav(sections);
                }
            }
        );
    }
})();

// save learned chapter
function addLearn() {
    var username = localStorage.getItem("username");
    var unitId = localStorage.getItem("unit");
    var chapterId = localStorage.getItem("chapter");
    if (username && unitId && chapterId) {
        // save
        $.post('http://localhost:5000/api/userLearn',
            {
                username: username,
                unitId: unitId,
                chapterId: chapterId
            },
            function (data) {
                if (data.code === 200) {
                    console.log(data);
                }
            }
        );
    }
}
