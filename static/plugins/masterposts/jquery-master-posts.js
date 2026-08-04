jQuery(document).ready(function(){
/*global jQuery:false */
/*jshint devel:true, laxcomma:true, smarttabs:true */
"use strict";



	/* clear fixes */
	jQuery('ul.mpbox.col3>li:nth-child(3n),ul.mpbox.col2>li:nth-child(2n),ul.mpbox.col4>li:nth-child(4n),ul.mpbox.col5>li:nth-child(5n),ul.mpbox.col6>li:nth-child(6n)').next().css({'clear': 'both'});


	/* add target blank */
	jQuery(".mp-staff ul.in-new-window>li>a").attr("target","_blank");
	jQuery(".mp-testimonials.in-new-window a").attr("target","_blank");
	jQuery(".mp-services.in-new-window a").attr("target","_blank");
	
	

	/* Tooltips */
	jQuery("body").prepend('<div class="tooltip"><p></p></div>');
	var tt = jQuery("div.tooltip");
	
	jQuery("ul.mp-staff-social li a").hover(function() {								
		var btn = jQuery(this);
			
			tt.children("p").text(btn.attr("title"));								
						
			var t = Math.floor(tt.outerWidth(true)/2),
				b = Math.floor(btn.outerWidth(true)/2),							
				y = btn.offset().top - 55,
				x = btn.offset().left - (t-b);
						
			tt.css({"top" : y+"px", "left" : x+"px", "display" : "block"});			
			   
		}, function() {		
			tt.hide();			
	});

/* the end */
});