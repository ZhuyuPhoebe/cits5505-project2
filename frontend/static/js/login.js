function login (e) {
	e.preventDefault();
	if (!CheckValid()) {
		return;
	}

	var user = $('input[name$="username"]').prop('value');
	var pw = $('input[name$="password"]').prop('value');
	$.post('http://localhost:5000/api/login',
	{'username': user,
	 'password': pw},
	function(data) {
		if(data.code === 200) {
			location.href="./index.html";
		}
		else {
			showErrorTip('Your account number or password is wrong!');
		}
	});
}

function CheckValid() {
	if($('input[name$="password"]').prop('value').length <= 0 ||
		$('input[name$="username"]').prop('value').length <= 0) {
		showErrorTip('Please fill out all fields');
		return false;
	}

	hideErrorTip();
	return true;
}

function showErrorTip(tip) {
	$('#error').text(tip);
	$('#error').show();
}

function hideErrorTip() {
	$('#error').text('');
	$('#error').hide();
}

function register (e) {
	e.preventDefault();
	if (!CheckValid()) {
		return;
	}

	var user = $('input[name$="username"]').prop('value');
	var pw = $('input[name$="password"]').prop('value');
	$.post('http://localhost:5000/api/register',
	{'username': user,
	 'password': pw},
	function(data) {
		if(data.code === 200) {
			alert('Registration succeeded!');
			location.href="./login.html";
		}
		else {
			showErrorTip(data.msg);
		}
	});
}