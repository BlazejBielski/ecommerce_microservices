import { useEffect, useState } from 'react';
import axios from 'axios';

export default function Reviews() {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    const productId = 1; // przykładowy product_id
    axios.get(`/api/v1/reviews/${productId}/`).then(res => {
      setReviews(res.data.results || []);
    });
  }, []);

  return (
    <div style={{ padding: '2rem' }}>
      <h2>⭐ Opinie o produkcie #1</h2>
      <ul>
        {reviews.length === 0 ? (
          <li>Brak recenzji</li>
        ) : (
          reviews.map(r => (
            <li key={r.id}><strong>{r.rating}/5</strong>: {r.comment}</li>
          ))
        )}
      </ul>
    </div>
  );
}