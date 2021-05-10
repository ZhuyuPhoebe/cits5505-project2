function renderQuestions(questions) {
    var html = '<form>';
    for (var i = 0; i < questions.length; i++) {
        if (questions[i][3] == 0) {
            html += '<div class="form-group">';
            html += '<label class="ques" id="' + questions[i][0] + '">' + (i + 1) + '. ' + questions[i][1] + '</label>';
            html += '<div class="radio"><label><input type="radio" name="' + questions[i][0] + '" value="' + questions[i][4][2] + '"/>' + questions[i][4][1] + '</label></div>';
            html += '<div class="radio"><label><input type="radio" name="' + questions[i][0] + '" value="' + questions[i][5][2] + '"/>' + questions[i][5][1] + '</label></div>';
            html += '<div class="radio"><label><input type="radio" name="' + questions[i][0] + '" value="' + questions[i][6][2] + '"/>' + questions[i][6][1] + '</label></div>';
            html += '<div class="radio"><label><input type="radio" name="' + questions[i][0] + '" value="' + questions[i][7][2] + '"/>' + questions[i][7][1] + '</label></div>';
            html += '</div>';
        } else {
            html += '<div class="form-group">';
            html += '<label class="ques" id="' + questions[i][0] + '">' + (i + 1) + '. ' + questions[i][1] + '</label>';
            html += '<div class="text">Your answer: <input class="text-questions" type="text" name="' + questions[i][0] + '" data-value="' + questions[i][4][1] + '"/></div>';
            html += '</div>';
        }
    }
    // add submit button
    html += '<div class="form-group"><input type="button" class="btn" onclick="mark(event)" value="Mark"/></div></form>';
    return html;
}

(function () {
    var quiz = localStorage.getItem("quiz");
    // get quiz
    if (quiz) {
        $.get('http://localhost:5000/api/quiz',
            {
                id: quiz
            },
            function (data) {
                if (data.code === 200) {
                    var units = data.data;

                    $('#quizTitle').append(units[1]);
                }
            });
        // get questions
        $.get('http://localhost:5000/api/questions',
            {
                id: quiz
            },
            function (data) {
                if (data.code === 200) {
                    var questions = data.data;
                    var questionsHtml = renderQuestions(questions);
                    $('#quiz').html(questionsHtml);
                }
            }
        );
    }
})();

function mark(e) {
    e.preventDefault();
    var ques = $("form").find('.ques');
    var total = ques.length;
    var correct = 0;
    for (var i = 0; i < ques.length; i++) {
        var name = ques[i].id;
        var checked = $('input:radio[name=' + name + ']:checked').val();

        // check answer
        if (checked == 1)
            correct++;
            
        // Check the blanks
        var textInput = $('input:text[name=' + name + ']');
        if ($(textInput).val() && $(textInput).val() == $(textInput).data('value')) {
            correct++;
            // Remove the original logo
            $(textInput).closest('div.text').find('span').remove();
            $(textInput).closest('div.text').find('p').remove();

            // Add a new logo
            var result = '<span class="glyphicon glyphicon-remove-sign text-success"></span><p class="text-success">The correct answer: ' + $(textInput).data('value') + '</p>';
            $(textInput).closest('div.text').append(result);
        } else {// Remove the original logo 
            $(textInput).closest('div.text').find('span').remove();
            $(textInput).closest('div.text').find('p').remove();
            
            // Add a new logo
            var result = '<span class="glyphicon glyphicon-remove-sign text-danger"></span><p class="text-success">The correct answer: ' + $(textInput).data('value') + '</p>';
            $(textInput).closest('div.text').append(result);
        }

        var inputs = $('input:radio[name=' + name + ']');
        for (var j = 0; j < inputs.length; j++) {
            var input = $(inputs[j]);
            // Show the correct answer 
            if (input.val() == 1) {
                $(input).closest('div.radio').addClass('has-success');
            }
        }
    }

    var username = localStorage.getItem("username");
    var quiz = localStorage.getItem("quiz");
    // score
    var score = (correct / total * 100).toFixed(2);
    // save user's score
    $.post('http://localhost:5000/api/userQuiz',
        {
            username: username,
            unitId: quiz,
            score: score
        },
        function (data) {
            if (data.code === 200) {
                console.log(data);
            }
        }
    );
    alert("Your score is:" + (score) + "%");
}

function backHome(e) {
    e.preventDefault();
    location.href = './learn.html';
}
