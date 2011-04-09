
// Set the callbacks for receipt of push messages

thywill.push.onReceipt = function(message) {
	
	console.log(message);
};

thywill.push.onError = function(error) {

	
};

// Set the callbacks for sending messages

thywill.send.onConfirm = function(confirmation) {
	
}

thywill.send.onError = function(error) {
	
	
}

// Functions to set up a trivial input form.
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

// Functions to set up an output canvas.
var setupOutput = function() {
	
}

// Set up the startup function and get things started.
thywill.application.fn = function() {
	setupInput();
	setupOutput();
};
thywill.application.ready();
