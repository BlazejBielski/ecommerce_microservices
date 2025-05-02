import { Link } from 'react-router-dom';

export default function App() {
  return (
    <div style={{ fontFamily: 'sans-serif', padding: '2rem' }}>
      <h1 style={{ fontSize: '2rem', marginBottom: '1rem' }}>🛒 Witaj w sklepie</h1>
      <nav style={{ display: 'flex', gap: '1rem' }}>
        <Link to="/login">🔐 Zaloguj się</Link>
        <Link to="/products">📦 Produkty</Link>
        <Link to="/cart">🛍️ Koszyk</Link>
        <Link to="/reviews">⭐ Recenzje</Link>
      </nav>
    </div>
  );
}