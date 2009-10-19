$('form').submit(function() {
	$this = $(this);
	$(this, 'input[type=submit').attr('disabled', 'disabled');
	$.ajax({
		data: $this.serialize(),
		    url: $this.attr('action'),
		    timeout: 2000,
	    })
    })