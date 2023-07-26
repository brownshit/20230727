import React, { useState } from 'react';
import MenuList from './MenuList';
import Cart from './Cart';

const App = () => {
  const initialMenus = [
    { id: 1, name: 'Menu 1', price: 10, image: 'menu1.png' },
    { id: 2, name: 'Menu 2', price: 15, image: 'menu2.jpg' },
    { id: 3, name: 'Menu 3', price: 12, image: 'menu3.jpg' },
  ];

  const [menus, setMenus] = useState(initialMenus);
  const [cartItems, setCartItems] = useState([]);

  const handleAddToCart = (menu) => {
    setCartItems([...cartItems, menu]);
  };

  const handleRemoveFromCart = (item) => {
    const updatedCartItems = cartItems.filter((menu) => menu.id !== item.id);
    setCartItems(updatedCartItems);
  };

  const handleCheckout = () => {
    // 여기에 결제로 넘어가는 코드 작성
  };

  return (
    <div className="app">
      <h1>Menu List</h1>
      <MenuList menus={menus} onAddToCart={handleAddToCart} />
      <Cart cartItems={cartItems} onRemoveFromCart={handleRemoveFromCart} onCheckout={handleCheckout} />
    </div>
  );
};

export default App;
