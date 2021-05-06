(function () {
    var quiz = sessionStorage.getItem("quiz");
    if (quiz) {
        $.get('http://localhost:5000/api/quiz',
        {
            id: quiz
        },
        function(data) {
            if(data.code === 200) {
                var units = data.data;
                
                $('#quizTitle').append(units[1]);
            }
        });
        $.get('http://localhost:5000/api/questions',
        {
            id: quiz
        },
        function(data) {
            if(data.code === 200) {
                var questions = data.data;
                var html = '<form>';
                for(var i=0;i<questions.length; i++){
                    html += '<div class="form-group">';
                    html += '<label class="ques" id="'+ questions[i][0] +'">'+ questions[i][1] +'</label>';
                    html += '<div class="radio"><label><input type="radio" name="'+ questions[i][0] +'" value="'+ questions[i][3][2] +'"/>'+ questions[i][3][1] +'</label></div>';
                    html += '<div class="radio"><label><input type="radio" name="'+ questions[i][0] +'" value="'+ questions[i][4][2] +'"/>'+ questions[i][4][1] +'</label></div>';
                    html += '<div class="radio"><label><input type="radio" name="'+ questions[i][0] +'" value="'+ questions[i][5][2] +'"/>'+ questions[i][5][1] +'</label></div>';
                    html += '<div class="radio"><label><input type="radio" name="'+ questions[i][0] +'" value="'+ questions[i][6][2] +'"/>'+ questions[i][6][1] +'</label></div>';
                    html += '</div>';
                }
                html += '<div class="form-group"><input type="button" class="btn" onclick="mark(event)" value="Mark"/></div></form>';
                $('#quiz').html(html);
            }
        });
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

        if (checked == 1)
            correct++;

        var inputs = $('input:radio[name=' + name + ']');
        for(var j = 0; j < inputs.length; j++) {
            var input = $(inputs[j]);
            if (input.val() == 1) {
                $(input).closest('div.radio').addClass('has-success');
            }
        }
    }

    var username = sessionStorage.getItem("username");
    var quiz = sessionStorage.getItem("quiz");
    var score = (correct / total * 100).toFixed(2);
    $.post('http://localhost:5000/api/userQuiz',
    {
        username: username,
        unitId: quiz,
        score: score
    },
    function(data) {
        if(data.code === 200) {
            console.log(data);
        }
    });
    alert("Your score is:" + (score) + "%");
}
