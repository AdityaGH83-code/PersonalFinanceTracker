'use client';

import { useEffect, useState } from 'react';
import { Expense } from '../lib/db';

export default function ExpenseList() {
  const [expenses, setExpenses] = useState<Expense[]>([]);

  useEffect(() => {
    fetch('/api/expenses')
      .then(res => res.json())
      .then(setExpenses)
      .catch(err => console.error('Error fetching expenses:', err));
  }, []);

  const handleDelete = async (id: number) => {
    await fetch(`/api/expenses/${id}`, { method: 'DELETE' });
    setExpenses(expenses.filter(e => e.id !== id));
  };

  return (
    <div className="mb-4">
      <h2 className="text-xl font-bold">Expenses</h2>
      <ul>
        {expenses.map(exp => (
          <li key={exp.id} className="mb-2 p-2 border">
            {exp.category}: ${exp.amount} on {exp.date} - {exp.description}
            <button onClick={() => handleDelete(exp.id!)} className="ml-2 bg-red-500 text-white px-2 py-1">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}