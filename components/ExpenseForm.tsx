'use client';

import { useState } from 'react';

export default function ExpenseForm() {
  const [category, setCategory] = useState('');
  const [amount, setAmount] = useState('');
  const [date, setDate] = useState(new Date().toISOString().slice(0, 10));
  const [description, setDescription] = useState('');

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    try {
      const res = await fetch('/api/expenses', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ category, amount: parseFloat(amount), date, description })
      });
      if (res.ok) {
        setCategory('');
        setAmount('');
        setDate('');
        setDescription('');
        window.location.reload();
      } else {
        alert('Error adding expense');
      }
    } catch (err) {
      console.error('Error:', err);
      alert('Error adding expense');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4 p-4 border">
      <input type="text" placeholder="Category" value={category} onChange={e => setCategory(e.target.value)} required className="mr-2" />
      <input type="number" placeholder="Amount" value={amount} onChange={e => setAmount(e.target.value)} required className="mr-2" />
      <input type="date" value={date} onChange={e => setDate(e.target.value)} required className="mr-2" />
      <input type="text" placeholder="Description" value={description} onChange={e => setDescription(e.target.value)} className="mr-2" />
      <button type="submit" className="bg-blue-500 text-white px-4 py-2">Add Expense</button>
    </form>
  );
}