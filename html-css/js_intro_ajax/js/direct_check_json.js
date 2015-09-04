/**
 * Created by jbroxton on 8/26/15
 * Modified for json on 9/4/15
  */


var inventory = document.getElementById("inventory");
var material, price;

var materials = [];

var xhr = new XMLHttpRequest();


xhr.onload = function() {
    console.log(xhr);
    if (xhr.status === 200) {
        var responseObject = JSON.parse(xhr.responseText); 
        var newItem = responseObject.inventory.item;
        console.log(responseObject.inventory.item);
        
        for (var i=0; i < newItem.length; i++){
            console.log(newItem.length);
            var newRow = '<tr>';
            newRow += "<td><input type='checkbox'/></td>";
            newRow += '<td>' + newItem[i].name + '</td>';
            newRow += '<td> $' + newItem[i].price + '</td>';
            newRow += '<td>' + newItem[i].numInStock + '</td>';
            newRow += '</tr>'; 
            inventory.innerHTML += newRow;
        }
    }
};

xhr.open('GET', 'js/stock.json', true);
xhr.send(null); 




function Product(name, stock, price) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function (num) {
        this.stock -= num;
    };

    this.inStock = function () {
        return this.stock > 0;
    };
}

populateInventoryDOM();

function populateInventoryDOM() {

    for (var i=0; i < materials.length; i++) {
        var newProdRow = document.createElement('tr');
        var checkboxcell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = materials[i].checked;
        checkboxcell.appendChild(checkbox);
        newProdRow.appendChild(checkboxcell);

        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(materials[i].name);
        nameCol.appendChild(nameText);
        newProdRow.appendChild(nameCol);

        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + materials[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        var stockCol = document.createElement('td');
        stockCol.className = materials[i].inStock();
        var stockText = document.createTextNode(materials[i].stock);
        stockCol.text = stockText;
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);
    }
}

function populateInventory() {

    var newRow = "";

    for (var i = 0; i < materials.length; i++) {
        newRow = "<tr>";
        newRow += "<td><input type='checkbox'/></td>";
        newRow += "<td>" + materials[i].name + '</td>';
        newRow += '<td>$' + materials[i].price + '</td>';
        if (materials[i].inStock()) {
           newRow += '<td class="true">Yes</td>';
        }
        else {
           newRow += '<td class="false">No</td>';
        }
        newRow += '<td>' + materials[i].stock + '</td>';
        newRow += '</tr>';
        inventory.innerHTML += newRow;
        rows = inventory.getElementsByTagName('tr');
        lastCheckboxList = rows[rows.length - 1].getElementsByTagName('input');
        lastCheckboxList[0].checked = materials[i].checked;
    }
}

function checkAll(checkbox) {
    var inputs = inventory.getElementsByTagName('input');
    if (checkbox.checked) {
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].checked = true;
           inputs[i].setAttribute('checked', '');
        }
    }
    else {
        for (var i = 0; i < inputs.length; i++) {
            inputs[i].checked = false;
           inputs[i].removeAttribute('checked');
        }
    }
}

function removeStock() {
    var rows = inventory.getElementsByTagName('tr');

    for (var i = 0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs.length > 0) {
            if (inputs[0].type == 'checkbox') {
                if (inputs[0].checked) {
                    var stock = rows[i].lastElementChild;
                    stock.className = 'false';
                    stock.textContent = 'No';
                    inputs[0].checked = false;
                }
            }
        }
    }
}

function addStock() {
    var rows = inventory.getElementsByTagName('tr');
    for (var i = 0; i < rows.length; i++) {
        console.log(rows);
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs.length > 0) {
            if (inputs[0].type == 'checkbox') {
                if (inputs[0].checked) {
                    var stock = rows[i].lastElementChild;
                    console.log(stock.textContent);
                    console.log(materials);
                    newStock = materials[i].stock + 1;
                    materials[i].stock = newStock;
                    stock.innerHTML = '<td>' + newStock.toString() + '</td>';
                    stock.className = 'true';
                    stock.textContent = 'Yes';
                    inputs[0].checked = false;
                }
            }
        }
    }
}

function addNewStock() {

    material = document.getElementById("material").value;
    price = document.getElementById("price").value;

    if (material == "" || price == "" || isNaN(price)) {
        return;
    }


    var newProdRow = document.createElement('tr');
    var checkboxcell = document.createElement('td');
    var checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.checked = false;
    checkboxcell.appendChild(checkbox);
    newProdRow.appendChild(checkboxcell);

    // Name Column
    var nameCol = document.createElement('td');
    var nameText = document.createTextNode(material);
    nameCol.appendChild(nameText);
    newProdRow.appendChild(nameCol);

    // Price Column
    var priceCol = document.createElement('td');
    var priceText = document.createTextNode('$' + price);
    priceCol.appendChild(priceText);
    newProdRow.appendChild(priceCol);

    // Stock Column
    var stockCol = document.createElement('td');
    stockCol.className = true;
    var stockText = document.createTextNode('10');
    stockCol.text = stockText;
    newProdRow.appendChild(stockCol);

    inventory.appendChild(newProdRow);
    materials.push(new Product(material, 10, parseInt(price)));


}
