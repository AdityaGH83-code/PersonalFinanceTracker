'use client';

import { Pie } from 'react-chartjs-2';
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

import { useEffect, useState } from 'react';

export default function Chart() {
  const [data, setData] = useState<any>({ labels: [], datasets: [] });

  useEffect(() => {
    fetch('/api/chart')
      .then(res => res.json())
      .then(({ labels, data: amounts }) => {
        setData({
          labels,
          datasets: [{
            data: amounts,
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF'],
          }]
        });
      })
      .catch(err => console.error('Error fetching chart data:', err));
  }, []);

  return (
    <div className="mb-4">
      <h2 className="text-xl font-bold">Spending by Category</h2>
      <Pie data={data} />
    </div>
  );
}