import React from 'react';

const CartItem = ({ item, onRemoveFromCart }) => {
  return (
    <div className="cart-item">
      <img src={item.image} alt={item.name} />
      <h3>{item.name}</h3>
      <p>Price: ${item.price}</p>
      <button onClick={() => onRemoveFromCart(item)}>Remove</button>
    </div>
  );
};

export default CartItem;
