
    const store = "Vastrika Fashion";
    let count = 0;
    let discount = 10;

    console.log("Store Name:", store);
    console.log("Initial Count:", count);
    console.log("Initial Discount:", discount);

    document.getElementById("storeName").innerText = store;
    document.getElementById("productCount").innerText = count;
    document.getElementById("discount").innerText = discount;

    function increaseCount() {
        count = count + 1;
        document.getElementById("productCount").innerText = count;
        console.log("Updated Count:", count);
    }

    const applyDiscount = function () {
        discount = discount + 5;
        document.getElementById("discount").innerText = discount;
        console.log("Updated Discount:", discount);
    };

    const calculatePrice = (price, discount) => {
        return price - (price * discount / 100);
    };

    let finalPrice = calculatePrice(1000, discount);
    console.log("Final Price:", finalPrice);
    // PROMPT
document.getElementById("nameBtn").addEventListener("click", function () {
    let name = prompt("Enter your name");

    if (name) {
        document.getElementById("userName").innerText = name;
        alert("Welcome " + name);
    }
});

// CONFIRM
document.getElementById("orderBtn").addEventListener("click", function () {
    let choice = confirm("Do you want to place order?");

    if (choice) {
        document.getElementById("msg").innerText = "Order Confirmed";
        alert("Order successful");
    } else {
        document.getElementById("msg").innerText = "Order Cancelled";
    }
});



