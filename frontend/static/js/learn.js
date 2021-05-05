(function () {
    var username = sessionStorage.getItem("username");
    var unitId = sessionStorage.getItem("unit");
    if (username && unitId) {
        $.get('http://localhost:5000/api/userLearn',
        {
            username: username,
            unitId: unitId
        },
        function(data) {
            if(data.code === 200) {
                var chapter = data.data;
                if (chapter) {
                    sessionStorage.setItem("chapter", chapter);
                    $('.chapter-item').removeClass('hidden');
                    $('#chapter').html(chapter);
                    $('#continue').html('<button class="btn" style="width: 200px;margin: -8px 0;">Continue Learn</button>');
                } else {
                    sessionStorage.removeItem("chapter");
                }
            }
        });
        $.get('http://localhost:5000/api/unitsById',
        {
            id: unitId
        },
        function(data) {
            if(data.code === 200) {
                var unit = data.data;
                $('#unitTitle').html(unit[1]);
                $('#unitOverview').html(unit[2]);
            }
        });
        $.get('http://localhost:5000/api/chapters',
        {
            id: unitId
        },
        function(data) {
            if(data.code === 200) {
                var chapters = data.data;
                var html = '';
                for(var i = 0; i < chapters.length; i++) {
                    var chapter = chapters[i];
                    var id = chapter[0];
                    var title = chapter[1];
                    var detail = chapter[2];
                    html += "<tr id='" + id + "'><td>" + id + "</td><td>" + title + "</td><td>" + detail + "</td><td><a class='btn' style='margin:12px 0;' data-id='"+ id +"' onclick='learn(event)' >Learn</a></td></tr>";
                        
                }
                $('#chapters').append(html);
            }
        });
        $.get('http://localhost:5000/api/userQuiz',
        {
            username: username,
            unitId: unitId
        },
        function(data) {
            if(data.code === 200) {
                var quizs = data.data;
                $('#quizNumber').html(quizs.length);
                $('.quiz-item').removeClass('hidden');
                $('.score-item').removeClass('hidden');
                var score = 0;
                for(var i = 0;i < quizs.length; i++) {
                    score += Number(quizs[i][2]);
                }
                var html = '';
                var average = (score / quizs.length).toFixed(2);
                if (average > 80) {
                    html = average + '<div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: '+ average +'%"><span class="sr-only">'+ average +'</span></div>';
                } else if (average > 60) {
                    html = average + '<div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: '+ average +'%"><span class="sr-only">'+ average +'</span></div>';
                } else if (average > 40) {
                    html = average + '<div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: '+ average +'%"><span class="sr-only">'+ average +'</span></div>';
                } else {
                    html = average + '<div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: '+ average +'%"><span class="sr-only">'+ average +'</span></div>';
                }
                $('.progress').html(html);
            }
        });
    }
})();

function learn (e) {
    e.preventDefault();
    var chapterId = $(e.target).data('id');
    sessionStorage.setItem("chapter", chapterId);
    location.href = './learnSections.html';
}


function continueLearn (e) {
    e.preventDefault();
    location.href = './learnSections.html';
}

function quiz (e) {
    e.preventDefault();
    var unitId = sessionStorage.getItem("unit");
    sessionStorage.setItem("quiz", unitId);
    location.href = './quiz.html';
}