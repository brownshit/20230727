import React from 'react';
import Menu from './Menu';

const MenuList = ({ menus, onAddToCart }) => {
  return (
    <div className="menu-list">
      {menus.map((menu) => (
        <Menu key={menu.id} menu={menu} onAddToCart={onAddToCart} />
      ))}
    </div>
  );
};

export default MenuList;
