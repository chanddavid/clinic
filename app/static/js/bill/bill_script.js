$(document).ready(function(){
	var actions = $("table.billtable td:last-child").html();
	// Append table with add row form on add new button click
    $(".add-bill").click(function(){
        console.log("adding")
		$(this).attr("disabled", "disabled");
		var index = $("table.billtable tbody tr:last-child").index();
        var row = '<tr>' +
            '<td><input type="number" class="form-control" name="sn" id="sn"></td>' +
            '<td><input type="text" class="form-control" name="particular" id="particular"></td>' +
            '<td><input type="number" class="form-control" name="rate" id="rate"></td>' +
            '<td><input type="number" class="form-control" name="qty" id="qty"></td>' +
            '<td><input type="number" class="form-control" name="total" id="total"></td>' +
			'<td>' + actions + '</td>' +
        '</tr>';
    	$("table.billtable").append(row);		
		$("table.billtable tbody tr").eq(index + 1).find(".add, .edit").toggle();
    });
	// Add row on add button click
	$(document).on("click", ".add", function(){
		var empty = false;
		var input = $(this).parents("tr").find('input[type="text"],input[type="number"]');
        input.each(function(){
			if(!$(this).val()){
				$(this).addClass("error");
				empty = true;
			} else{
                $(this).removeClass("error");
            }
		});
		$(this).parents("tr").find(".error").first().focus();
		if(!empty){
			input.each(function(){
				$(this).parent("td").html($(this).val());
			});			
			$(this).parents("tr").find(".add, .edit").toggle();
			$(".add-bill").removeAttr("disabled");
		}		
    });
	// Edit row on edit button click
	$(document).on("click", ".edit", function(){		
        $(this).parents("tr").find("td:not(:last-child)").each(function(){
			$(this).html('<input type="text" class="form-control" value="' + $(this).text() + '">');
		});		
		$(this).parents("tr").find(".add, .edit").toggle();
		$(".add-bill").attr("disabled", "disabled");
    });
	// Delete row on delete button click
	$(document).on("click", ".delete", function(){
        $(this).parents("tr").remove();
		$(".add-bill").removeAttr("disabled");
    });
});
