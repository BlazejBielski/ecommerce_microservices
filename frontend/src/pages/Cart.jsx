import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Cart() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const auth = localStorage.getItem('access');
    axios.get('/api/v1/cart/', {
      headers: { Authorization: `Bearer ${auth}` }
    }).then(res => setItems(res.data.results || []));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>🛍️ Twój koszyk</h2>
      <ul>
        {items.length === 0 ? (
          <li>Brak produktów w koszyku</li>
        ) : (
          items.map((item, i) => (
            <li key={i}>Produkt ID: {item.product_id}</li>
          ))
        )}
      </ul>
    </div>
  );
}