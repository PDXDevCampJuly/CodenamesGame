//var list = ["0","1","2","3","4","5","6"];
//
//(function create_board(){
//    var list = ["0","1","2","3","4","5","6"];
//
//    var table = document.getElementById('boardwrapper'); //Appends table to html
//
//    var new_table = document.createElement('table');
//
//    for (var i = 0; i < 5; i++){
//        var new_tr = document.createElement('tr'); //creates new tr
//        for(var j = 0; j <= 4; j++){
//
//            var new_td = document.createElement('td'); //creates new td
//
//            new_td.textContent=list[j];
//
//            new_tr.appendChild(new_td); //appends td to tr
//        }
//
//        new_table.appendChild(new_tr);
//        table.appendChild(new_table); //appends table to html
//    }
//}());



$.getJSON( "../../docs/test.json", function( data ) {
    console.log("Yoooooo");
    var list = [];
    for (var i = 0; i < 24; i++) {
        list.push(data.test[i]);
        console.log(data.test[i])
    }
    function create_board(list){

        var table = document.getElementById('boardwrapper'); //Appends table to html

        var new_table = document.createElement('table');

        for (var i = 0; i < 5; i++){
            var new_tr = document.createElement('tr'); //creates new tr
            for(var j = 0; j <= 4; j++){

                var new_td = document.createElement('td'); //creates new td

                new_td.textContent=list[j];

                new_tr.appendChild(new_td); //appends td to tr
            }

            new_table.appendChild(new_tr);
            table.appendChild(new_table); //appends table to html
            }
        }

create_board(list)

});



//  $( "<ul/>", {
//    "class": "my-new-list",
//    html: items.join( "" )
//  }).appendTo( "body" );
//});


//Make the ajax call

//Loop through it 25 times

//  Every time I want it to make a random number(0-25), and append the index of that random number to list
//(function () {
//    $.ajax({
//        url: "../../../docs/test.json", //Whatever the path to our json file is
//        type: "GET",
//        dataType: "json",
//        complete: function(data) {
//            var response = data.responseJSON.parse;
//            for (var i=0; i < 24; i++) {
//                var words = data.response.;
//
//                var x = Math.floor((Math.random() * 25) + 1);
//
//                var list = [];
//
//                list.append(response[x]);
//
//            function create_board(list){
//
//                var table = document.getElementById('boardwrapper'); //Appends table to html
//
//                var new_table = document.createElement('table');
//
//                for (var i = 0; i < 5; i++){
//                    var new_tr = document.createElement('tr'); //creates new tr
//                    for(var j = 0; j <= 4; j++){
//
//                        var new_td = document.createElement('td'); //creates new td
//
//                        new_td.textContent=list[j];
//
//                        new_tr.appendChild(new_td); //appends td to tr
//                    }
//
//                    new_table.appendChild(new_tr);
//                    table.appendChild(new_table); //appends table to html
//                    }
//                }
//
//                create_board(list)
//
//            }
//        }
//    })
//}());

//Make a ajax call
// take 25 items from the json file
// put them in list
