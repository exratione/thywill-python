
// Set the callbacks for receipt of push messages

thywill.push.onReceipt = function(message) {
	$("#poc-output").append("<br/><span>" + message + "</span>")
	if( console.log ) {	
		console.log(message);
	}
};
thywill.push.onError = function(error) {

	
};

// Set the callbacks for sending messages

thywill.send.onConfirm = function(confirmation) {
	// do nothing
}
thywill.send.onError = function(error) {
	if( console.log ) {
		console.log(error);
	}
}

// Set up a trivial input form.
var setupInput = function() {
	$("body").append(
		'<div id="sender">' +
			'<textarea></textarea>'	+
			'<button>Send</button>' +
		'</div>'
	);
	$("#sender button").click(function() {
		var message = $("#sender textarea").val();
		if( message ) {
			thywill.send.fn(message);
			$("#sender textarea").html("");
		}
	});
};

// Set up an output area
var setupOutput = function() {
	$("body").append('<div id="poc-output" style="margin-top: 10px; width: 500px; height: 200px; overflow-y: scroll; border: 1px solid #cccccc;"></div>');
}

// Set the startup function and declare readiness.
thywill.application.fn = function() {
	setupInput();
	setupOutput();
};
thywill.application.ready();
