function tableSearch() {
    var phrase = document.getElementById('search-text');
    var table = document.getElementById('table-id');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        for (var j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }
    }
}

function tableSearchForEmotion() {
    var phrase = document.getElementById('select_emotion');
    var table = document.getElementById('table-id');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        flag = regPhrase.test(table.rows[i].cells[3].innerHTML);
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }
    }
}

function tableSearchForDate() {
    var phrase = document.getElementById('date_selector');
    var table = document.getElementById('table-id');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        flag = regPhrase.test(table.rows[i].cells[5].innerHTML);
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }
    }
}
