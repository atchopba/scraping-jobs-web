$(document).ready(function(){

    // autocompletion
    $("#searchcity").autocomplete({

        source: function(request, response) {
            
            $.ajax({
                url: "/extract_city",
                type: 'POST',
                dataType: 'json',
                data: {
                    search_city: $("#searchcity").val()
                },
                success: function(data) {
                    response($.map(data, function(obj) {
                        return obj.name +" ("+ obj.department_code +")";
                    }));
                },
                error: function(result, status, error) {
                    console.log('Extract city rror : ');
                    console.log(error);
                }
            });

        },
        minLength: 3,
        position : {
            at : 'bottom',
            my : 'top'
        },
        select : function(event, ui){ // lors de la sélection d'une proposition
            //console.log("=> select : ", ui);
        }
    });

    // bouton rechercher
	$("#btnsearch").click(function() {

        searchlib = $("#searchlib").val().trim();
        searchcity = $("#searchcity").val().trim();

        if (searchlib == "" || searchcity == "") {
            alert("Renseigner le libellé et la ville, s'il vous plait !");
            return;
        }

        $("#boxresult").html("recherche en cours ... 1min max de patience!");

    	$.ajax({
    		url: "/scraping_job",
    		type: "POST",
    		data: {
    			q: searchlib,
    			city: searchcity,
    			contract: $("#searchcontract").val().trim()
    		},
    		success : function(data) {
    			$("#boxresult").html(data);
    		},
    		error: function(result, status, error) {
				alert("Une erreur est survenue. Veuillez ressayer!");
                console.log('=> error : ', error);
			}
    	});

  	});

});