// frontend/components/OrderDetails.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const OrderDetails = ({ orderId }) => {
  const [orderDetails, setOrderDetails] = useState(null);

  useEffect(() => {
    // API 주소와 함께 주문 상세 정보 요청
    axios.get(`/api/get_order_details/${orderId}/`)
      .then(response => {
        setOrderDetails(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, [orderId]);

  if (!orderDetails) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      {/* 주문 상세 정보 화면 구성 */}
    </div>
  );
};

export default OrderDetails;
