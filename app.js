process = function(text) {
	$.ajax({
		url: "http://localhost:5000/process_words",
			context: document.body,
			data: { 'text': text }
		}).done(function(ret) {
			console.log(ret.response);
			$('#visual-dest').html(ret.response);
			return ret.response
		});
}

$(document).ready(function() {
	$('#text-to-visualize').keyup(function() {
		text = $(this).val();
			
		out_text = process(text);
		console.log(out_text);
		$('#visual-dest').html(out_text);
	});
})