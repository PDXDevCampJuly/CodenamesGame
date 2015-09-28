

$(function create_board() {

    var table = document.getElementById('boardwrapper'); //Appends table to html

    var new_table = document.createElement('table');

        for (var i = 0; i < 5; i++) {
            var new_tr = document.createElement('tr'); //creates new tr

            for (var j = 0; j <= 4; j++) {

                var new_td = document.createElement('td'); //creates new td
                        new_td.textContent = test[j + i * 5]; //Saves the correct card indexes


                        new_tr.appendChild(new_td); //appends td to tr

                    new_table.appendChild(new_tr);
                    table.appendChild(new_table); //appends table to html

        }
    }
});