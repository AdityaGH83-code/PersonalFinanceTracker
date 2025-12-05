import { NextResponse } from 'next/server';
import db from '../../../lib/db';

export async function GET() {
    const expenses = db.prepare('SELECT * FROM expenses').all() as any[];

    // Group by category
    const categoryTotals: { [key: string]: number } = {};
    const categoryCounts: { [key: string]: number } = {};
    expenses.forEach(exp => {
        categoryTotals[exp.category] = (categoryTotals[exp.category] || 0) + exp.amount;
        categoryCounts[exp.category] = (categoryCounts[exp.category] || 0) + 1;
    });

    const categoryAverages = Object.keys(categoryTotals).reduce((acc, cat) => {
        acc[cat] = categoryTotals[cat] / categoryCounts[cat];
        return acc;
    }, {} as { [key: string]: number });

    // Anomalies: expenses where amount > 1.5 * average for category
    const anomalies = expenses.filter(exp => exp.amount > 1.5 * categoryAverages[exp.category]);

    // Suggestions: if total for category > 1000, suggest reduce
    const suggestions = Object.keys(categoryTotals).filter(cat => categoryTotals[cat] > 1000).map(cat => `Consider reducing spending in ${cat}`);

    return NextResponse.json({
        categoryTotals,
        anomalies,
        suggestions
    });
}