/**
 * Set up the connection to Orbited, using the STOMP client.
 */
// For why this is done, see: http://stackoverflow.com/questions/1481251/what-does-document-domain-document-domain-do 
document.domain = document.domain;

// If TCPSocket is not set, the Orbited Javascript files will error on load.
TCPSocket = Orbited.TCPSocket;

thywill.push.stomp = new STOMPClient();
thywill.push.stomp.onopen = function() {
	// This callback indicates a connection is established, so now subscribe to the client channel,
	// and notify the framework that matters are set up.
	thywill.push.stomp.subscribe(thywill.config.uuid);
	thywill.push.onEstablishConnectionComplete();
};
thywill.push.stomp.onclose = function(code) {
    //shell.print("Transport closed (code: " + code + ")");
};
thywill.push.stomp.onerror = function(error) {
	thywill.push.onError(error);
};
thywill.push.stomp.onerrorframe = function(frame) {
	thywill.push.onError(frame.body);
};
thywill.push.stomp.onconnectedframe = function() {

};
thywill.push.stomp.onmessageframe = function(frame) {
	thywill.push.onReceipt(frame.body);
};

$(window).unload(function() {
	// it is possible that neither of these is necessary.
	//thywill.push.stomp.disconnect();
	//thywill.push.stomp.reset();
});

thywill.push.establishConnection = function() {
	 // once connection is established then stomp.onopen() is called
	thywill.push.stomp.connect(
		thywill.config.bootstrap_parameters.stomp_hostname, 
		thywill.config.bootstrap_parameters.stomp_port, 
		'guest', 
		'guest'
	);
};