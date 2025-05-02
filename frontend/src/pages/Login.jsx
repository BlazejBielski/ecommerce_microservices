import { useState } from 'react';
import axios from 'axios';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  async function handleSubmit(e) {
    e.preventDefault();
    try {
      const res = await axios.post('/api/v1/token/', { email, password });
      localStorage.setItem('access', res.data.access);
      alert('Zalogowano!');
    } catch (err) {
      alert('Błąd logowania');
    }
  }

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '300px', margin: '2rem auto' }}>
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} style={{ marginBottom: '1rem' }} />
      <input type="password" placeholder="Hasło" value={password} onChange={e => setPassword(e.target.value)} style={{ marginBottom: '1rem' }} />
      <button type="submit">Zaloguj</button>
    </form>
  );
}