$("textarea").each(function(textarea) {
    $(this).height( $(this).scrollHeight );
});

function handleFileSelect(inputId, outputId) {               
	if (!window.File || !window.FileReader || !window.FileList || !window.Blob) {
	  alert('The File APIs are not fully supported in this browser.');
	  return;
	}

	input = document.getElementById(inputId);
	if (!input) {
	  alert("Um, couldn't find the element.");
	}
	else if (!input.files) {
	  alert("This browser doesn't seem to support the `files` property of file inputs.");
	}
	else if (!input.files[0]) {
	  alert("Please select a file before clicking 'Load'");               
	}
	else {
	  file = input.files[0];
	  fr = new FileReader();
	  fr.onload = function() {
	  	$('#' + outputId).val(fr.result)
	  };
	  fr.readAsText(file);
	}
}
