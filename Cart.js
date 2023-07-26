import React from 'react';
import CartItem from './CartItem';

const Cart = ({ cartItems, onRemoveFromCart, onCheckout }) => {
  const totalPrice = cartItems.reduce((acc, item) => acc + item.price, 0);

  return (
    <div className="cart">
      <h2>Cart</h2>
      {cartItems.map((item) => (
        <CartItem key={item.id} item={item} onRemoveFromCart={onRemoveFromCart} />
      ))}
      <p>Total Price: ${totalPrice}</p>
      <button onClick={onCheckout}>Checkout</button>
    </div>
  );
};

export default Cart;
