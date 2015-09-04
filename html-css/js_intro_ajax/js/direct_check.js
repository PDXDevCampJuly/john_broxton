/**
 * Created by jbroxton on 8/26/15.
 */

var inventory = document.getElementById('inventory');
var woodStock, material, price;

//        var product = {
//            checked: false,
//            name: 'Wood',
//            stock: 10,
//            price: 15,
//
//            adjustStock: function(num) {
//                this.stock -= num;
//            },
//
//            inStock: function() {
//                return this.stock > 0;
//            }
//
//        };

        //console.log(product);
        //product.adjustStock(2);
        //console.log(product.stock);
        //console.log(product.inStock());

function Product(name, stock, price) {
    this.checked = false;
    this.name = name;
    this.stock = stock;
    this.price = price;

    this.adjustStock = function(num) {
        this.stock -= num;
    }

    this.inStock = function () {
        return this.stock > 0;
    }
}

var materials = [new Product('wood', 5 , 30), new Product('glass', 10, 5), new Product('asbestos', 0, 30)];

populateInventory();

populateInventoryDOM();

function populateInventoryDOM() {
    for (var i=0; i < materials.length; i++) {
        var newProdRow = document.createElement('tr');

        //checkbox column
        var checkboxCell = document.createElement('td');
        var checkbox = document.createElement('input');
        checkbox.type = "checkbox";
        checkbox.checked = materials[i].checked;
        checkboxCell.appendChild(checkbox);
        newProdRow.appendChild(checkboxCell);

        //name column
        var nameCol = document.createElement('td');
        var nameText = document.createTextNode(materials[i].name);
        nameCol.appendChild(nameText);
        newProdRow.appendChild(nameCol);

        //price column
        var priceCol = document.createElement('td');
        var priceText = document.createTextNode('$' + materials[i].price);
        priceCol.appendChild(priceText);
        newProdRow.appendChild(priceCol);

        //stock column
        var stockCol = document.createElement('td');
        stockCol.className = 'true';
        var stockText = document.createTextNode(materials[i].stock);
        stockCol.appendChild(stockText);
        newProdRow.appendChild(stockCol);

        inventory.appendChild(newProdRow);

    }
}


function populateInventory() {
    //Loop through materials
    //Add a row for each item in materials'+
    //Make sure that stock class reflects inStock
    //Make sure that checkbox status reflects checked

    for (var i=0; i < materials.length; i++) {
            var newRow = "<tr>";
            newRow += '<td><input type="checkbox"/></td>';
            newRow += '<td>' + materials[i].name + '</td>';
            newRow += '<td>' + materials[i].price + '</td>';
            newRow += '<td class="'+ materials[i].inStock() +'">' + materials[i].stock + '</td>';
            newRow += '</tr>';

            inventory.innerHTML += newRow;

            if (materials[i].type == 'checkbox') {
                materials[i].checked = true;
            }



    }
}

function removeStock() {

    var rows = inventory.getElementsByTagName('tr');

    for (var i=0; i < rows.length; i++) {
        console.log(rows[i]);
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type == 'checkbox') {
            if (inputs[0].checked){
                //Flip the status of the stocked column
                var stock = rows[i].lastElementChild;
                stock.className = 'false';
                stock.textContent = 'No';
            }
        }
    }
}

function addStock() {

    var rows = inventory.getElementsByTagName('tr');

    for (var i=0; i < rows.length; i++) {
        var inputs = rows[i].getElementsByTagName('input');
        if (inputs[0].type == 'checkbox') {
            if (inputs[0].checked) {
                //Flip the status of the stocked column
                var stock = rows[i].lastElementChild;
                stock.className = 'true';
                stock.textContent = 'Yes';
            }
        }
    }
}

function checkAll(check_all) {

    var inputs = inventory.getElementsByTagName('input');

    for (var i=0; i < inputs.length; i++) {
        if (inputs[i].type == 'checkbox') {
        inputs[i].checked = check_all.checked;
        }
    }
}

function addNewStock() {
    material = document.getElementById('material').value;
    price = document.getElementById('price').value;

    if (material === "" || price === '' || isNaN(price)) {
        return
    }


    var newProdRow = document.createElement('tr');

    //checkbox column
    var checkboxCell = document.createElement('td');
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.checked = materials[i].checked;
    checkboxCell.appendChild(checkbox);
    newProdRow.appendChild(checkboxCell);

    //name column
    var nameCol = document.createElement('td');
    var nameText = document.createTextNode(material);
    nameCol.appendChild(nameText);
    newProdRow.appendChild(nameCol);

    //price column
    var priceCol = document.createElement('td');
    var priceText = document.createTextNode('$' + materials[i].price);
    priceCol.appendChild(priceText);
    newProdRow.appendChild(priceCol);

    //stock column
    var stockCol = document.createElement('td');
    stockCol.className = 'true';
    var stockText = document.createTextNode('10');
    stockCol.appendChild(stockText);
    newProdRow.appendChild(stockCol);

    inventory.appendChild(newProdRow);
    materials.push(new Product(material, 10, price));

    document.getElementById('material').value = "";
    document.getElementById('price').value = "";


    console.log("This is material and price " + material + ' ' + price);

    if (material == "") {
        return false
    }

    if (price == "") {
        return false
    }

    price = parseInt(price);
    if (price != parseInt(price)) {
        return false
    }


    //var newRow = "<tr>";
    //newRow += '<td><input type="checkbox"/></td>';
    //newRow += '<td>' + material + '</td>';`
    //newRow += '<td>' + price + '</td>';
    //newRow += '<td class="false">No</td>';
    //newRow += '</tr>';
    //
    //inventory.innerHTML += newRow;

}