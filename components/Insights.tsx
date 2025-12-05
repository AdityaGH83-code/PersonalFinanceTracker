'use client';

import { useEffect, useState } from 'react';

export default function Insights() {
  const [insights, setInsights] = useState<any>({});

  useEffect(() => {
    fetch('/api/insights')
      .then(res => res.json())
      .then(setInsights)
      .catch(err => console.error('Error fetching insights:', err));
  }, []);

  return (
    <div className="mb-4 p-4 border">
      <h2 className="text-xl font-bold">Budget Insights</h2>
      <h3 className="font-semibold">Totals by Category:</h3>
      <ul>
        {Object.entries(insights.categoryTotals || {}).map(([cat, total]) => (
          <li key={cat}>{cat}: ${total as number}</li>
        ))}
      </ul>
      <h3 className="font-semibold">Anomalies (unusual expenses):</h3>
      <ul>
        {insights.anomalies?.map((exp: any) => (
          <li key={exp.id}>{exp.category}: ${exp.amount} on {exp.date} - {exp.description}</li>
        ))}
      </ul>
      <h3 className="font-semibold">Suggestions:</h3>
      <ul>
        {insights.suggestions?.map((sug: string, i: number) => (
          <li key={i}>{sug}</li>
        ))}
      </ul>
    </div>
  );
}