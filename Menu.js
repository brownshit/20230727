import React from 'react';

const Menu = ({ menu, onAddToCart }) => {
  return (
    <div className="menu-item">
      <img src="{% static 'menu1.png' %}" alt="burger" />
      <h3>{menu.name}</h3>
      <p>Price: ${menu.price}</p>
      <button onClick={() => onAddToCart(menu)}>Add to Cart</button>
    </div>
  );
};

export default Menu;
