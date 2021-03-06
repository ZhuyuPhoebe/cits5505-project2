function login(e) {
	e.preventDefault();
	// check valid
	if (!CheckValid()) {
		return;
	}

	var user = $('input[name$="username"]').prop('value');
	var pw = $('input[name$="password"]').prop('value');
	$.post('http://localhost:5000/api/login',
		{
			'username': user,
			'password': pw
		},
		function (data) {
			if (data.code === 200) {
				// storage username
				localStorage.setItem("username", user);
				location.href = "http://localhost:5000/";
			}
			else {
				showErrorTip('Your account number or password is wrong!');
			}
		}
	);
}

function CheckValid() {
	// username and password is reuqired
	if ($('input[name$="password"]').prop('value').length <= 0 ||
		$('input[name$="username"]').prop('value').length <= 0) {
		showErrorTip('Please fill out all fields');
		return false;
	}

	hideErrorTip();
	return true;
}

// show error
function showErrorTip(tip) {
	$('#error').text(tip);
	$('#error').show();
}

// hide error
function hideErrorTip() {
	$('#error').text('');
	$('#error').hide();
}

function register(e) {
	e.preventDefault();
	if (!CheckValid()) {
		return;
	}

	var user = $('input[name$="username"]').prop('value');
	var pw = $('input[name$="password"]').prop('value');
	$.post('http://localhost:5000/api/register',
		{
			'username': user,
			'password': pw
		},
		function (data) {
			if (data.code === 200) {
				alert('Registration succeeded!');
				// redirect to login
				location.href = "http://localhost:5000/login";
			}
			else {
				showErrorTip(data.msg);
			}
		}
	);
}
