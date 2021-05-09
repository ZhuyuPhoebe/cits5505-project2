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
                    var html = '<div>';
                    for (var i = 0; i < sections.length; i++) {
                        var chapter = sections[i];
                        var id = chapter[0];
                        var title = chapter[1];
                        var detail = chapter[2];
                        html += "<h4>" + title + "</h4>";
                        html += "<p>" + detail + "</p><hr />";
                    }
                    html += '</div>';
                    // Append to DOM
                    $('#learn').append(html);
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
