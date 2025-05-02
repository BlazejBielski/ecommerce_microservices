import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Products() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get('/api/v1/products/').then(res => setProducts(res.data.results));
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>📦 Produkty</h2>
      <ul>
        {products.map(p => (
          <li key={p.id}>{p.name} - {p.price}</li>
        ))}
      </ul>
    </div>
  );
}