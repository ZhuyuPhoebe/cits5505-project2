(function () {
    var username = sessionStorage.getItem("username");
    var chapterId = sessionStorage.getItem("chapter");
    if (username && chapterId) {
        $.get('http://localhost:5000/api/sections',
        {
            id: chapterId
        },
        function(data) {
            if(data.code === 200) {
                var sections = data.data;
                var html = '<div>';
                for(var i = 0; i < sections.length; i++) {
                    var chapter = sections[i];
                    var id = chapter[0];
                    var title = chapter[1];
                    var detail = chapter[2];
                    html += "<h4>" + title + "</h4><p>" + detail + "</p><hr />";
                }
                html += '</div>';
                $('#learn').append(html);
            }
        });
    }
})();

function addLearn () {
    var username = sessionStorage.getItem("username");
    var unitId = sessionStorage.getItem("unit");
    var chapterId = sessionStorage.getItem("chapter");
    if (username && unitId && chapterId) {
        $.post('http://localhost:5000/api/userLearn',
        {
            username: username,
            unitId: unitId,
            chapterId: chapterId
        },
        function(data) {
            if(data.code === 200) {
                console.log(data);
            }
        });
    }
}