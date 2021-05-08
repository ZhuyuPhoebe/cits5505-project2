(function () {
    // get username and unit id
    var username = localStorage.getItem("username");
    var unitId = localStorage.getItem("unit");
    if (username && unitId) {
        // get the learned chapter
        $.get('http://localhost:5000/api/userLearn',
            {
                username: username,
                unitId: unitId
            },
            function (data) {
                if (data.code === 200) {
                    var chapter = data.data;
                    if (chapter) {
                        localStorage.setItem("chapter", chapter);

                        // Show the learned chapter
                        $('.chapter-item').removeClass('hidden');
                        $('#chapter').html(chapter);

                        // append continue button
                        $('#continue').html('<button class="btn" style="width: 200px;margin: -8px 0;">Continue Learn</button>');
                    } else {
                        localStorage.removeItem("chapter");
                    }
                }
            }
        );

        // get unit detail
        $.get('http://localhost:5000/api/unitsById',
            {
                id: unitId
            },
            function (data) {
                if (data.code === 200) {
                    var unit = data.data;
                    // append unit title and overview
                    $('#unitTitle').html(unit[1]);
                    $('#unitOverview').html(unit[2]);
                }
            }
        );

        // get chapters
        $.get('http://localhost:5000/api/chapters',
            {
                id: unitId
            },
            function (data) {
                if (data.code === 200) {
                    var chapters = data.data;
                    var html = '';
                    for (var i = 0; i < chapters.length; i++) {
                        var chapter = chapters[i];
                        var id = chapter[0];
                        var title = chapter[1];
                        var detail = chapter[2];
                        html += "<tr id='" + id + "'>";
                        html += "<td>" + id + "</td>";
                        html += "<td>" + title + "</td>";
                        html += "<td>" + detail + "</td>";
                        html += "<td>";
                        // Add buttons for learning chapters
                        html += "<a class='btn' style='margin:12px 0;' data-id='" + id + "' onclick='learn(event)' >Learn</a>";
                        html += "</td>";
                        html += "</tr>";
                    }
                    // append to DOM
                    $('#chapters').append(html);
                }
            }
        );
        // Get the user's grades
        $.get('http://localhost:5000/api/userQuiz',
            {
                username: username,
                unitId: unitId
            },
            function (data) {
                if (data.code === 200) {
                    var quizs = data.data;
                    $('#quizNumber').html(quizs.length);
                    // show quiz and score
                    $('.quiz-item').removeClass('hidden');
                    $('.score-item').removeClass('hidden');

                    // Calculate the average score
                    var score = 0;
                    for (var i = 0; i < quizs.length; i++) {
                        score += Number(quizs[i][2]);
                    }

                    // append score progress bar
                    var html = '';
                    var average = (score / quizs.length).toFixed(2);
                    if (average > 80) {
                        html = average + '<div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100" style="width: ' + average + '%">';
                        html += '<span class="sr-only">' + average + '</span>';
                        html += '</div>';
                    } else if (average > 60) {
                        html = average + '<div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100" style="width: ' + average + '%">';
                        html += '<span class="sr-only">' + average + '</span>';
                        html += '</div>';
                    } else if (average > 40) {
                        html = average + '<div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100" style="width: ' + average + '%">';
                        html += '<span class="sr-only">' + average + '</span>';
                        html += '</div>';
                    } else {
                        html = average + '<div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" style="width: ' + average + '%">';
                        html += '<span class="sr-only">' + average + '</span>';
                        html += '</div>';
                    }
                    // append to DOM
                    $('.progress').html(html);
                }
            }
        );
    }
})();

// Redirect to learning page
function learn(e) {
    e.preventDefault();
    var chapterId = $(e.target).data('id');
    // storage chapter id
    localStorage.setItem("chapter", chapterId);
    location.href = './learnSections.html';
}

// Redirect to learning page
function continueLearn(e) {
    e.preventDefault();
    location.href = './learnSections.html';
}

// Redirect to quiz page
function quiz(e) {
    e.preventDefault();
    var unitId = localStorage.getItem("unit");
    // Storage quiz id
    localStorage.setItem("quiz", unitId);
    location.href = './quiz.html';
}