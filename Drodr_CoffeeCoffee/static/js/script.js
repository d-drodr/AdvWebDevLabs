// script.js

// Function to add an item to the cart
function addToCart(itemId, itemName, itemPrice) {
    // Check if the item is already in the cart
    const existingCartItem = getCartItem(itemId);
  
    if (existingCartItem) {
      // If the item already exists, increment its quantity
      existingCartItem.quantity += 1;
    } else {
      // If the item is not in the cart, create a new cart item
      const cartItem = {
        id: itemId,
        name: itemName,
        price: itemPrice,
        quantity: 1,
      };
      cart.push(cartItem);
    }
  
    // Update the cart display
    updateCartDisplay();
  }
  
  // Function to remove an item from the cart
  function removeFromCart(itemId) {
    // Find the index of the item in the cart
    const itemIndex = cart.findIndex(item => item.id === itemId);
  
    if (itemIndex !== -1) {
      // Remove the item from the cart
      cart.splice(itemIndex, 1);
    }
  
    // Update the cart display
    updateCartDisplay();
  }
  
  // Function to get the cart item by its ID
  function getCartItem(itemId) {
    return cart.find(item => item.id === itemId);
  }
  
  // Function to update the quantity of a cart item
  function updateCartItemQuantity(itemId, quantity) {
    const cartItem = getCartItem(itemId);
  
    if (cartItem) {
      cartItem.quantity = quantity;
    }
  
    // Update the cart display
    updateCartDisplay();
  }
  
  // Function to calculate the total price of items in the cart
  function calculateTotalPrice() {
    let totalPrice = 0;
  
    for (const item of cart) {
      totalPrice += item.price * item.quantity;
    }
  
    return totalPrice;
  }
  
  // Function to update the cart display
  function updateCartDisplay() {
    // Get the cart element
    const cartElement = document.getElementById('cart');
  
    // Clear the cart element
    cartElement.innerHTML = '';
  
    // Render each cart item in the cart element
    for (const item of cart) {
      const itemElement = document.createElement('div');
      itemElement.className = 'cart-item';
      itemElement.innerHTML = `
        <span>${item.name}</span>
        <span>${item.price}</span>
        <input type="number" value="${item.quantity}" min="1" onchange="updateCartItemQuantity(${item.id}, this.value)">
        <button onclick="removeFromCart(${item.id})">Remove</button>
      `;
      cartElement.appendChild(itemElement);
    }
  
    // Update the total price
    const totalPrice = calculateTotalPrice();
    const totalPriceElement = document.getElementById('total-price');
    totalPriceElement.textContent = `Total Price: $${totalPrice.toFixed(2)}`;
  }
  