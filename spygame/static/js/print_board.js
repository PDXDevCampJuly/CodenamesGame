
function create_board(){
    var list = ["0","1","2","3","4","5","6","7", "8", "9", "10", "11", "12","13","14","15","16","17", "18", "19", "20", "21","22","23", "24","25"];

    var table = document.getElementById('boardwrapper'); //Appends table to html

    var new_table = document.createElement('table');

    for (var i = 0; i < 5; i++){
        var new_tr = document.createElement('tr'); //creates new tr

        for(var j = 0; j <= 4; j++){

            var new_td = document.createElement('td'); //creates new td

            new_td.textContent=list[5*i +j]; //Saves the correct card indexes

            new_tr.appendChild(new_td); //appends td to tr
        }

        new_table.appendChild(new_tr);
        table.appendChild(new_table); //appends table to html
    }
}

create_board()

