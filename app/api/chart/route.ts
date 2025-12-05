import { NextResponse } from 'next/server';
import db from '../../../lib/db';

export async function GET() {
    const expenses = db.prepare('SELECT * FROM expenses').all() as any[];

    const categoryTotals: { [key: string]: number } = {};
    expenses.forEach(exp => {
        categoryTotals[exp.category] = (categoryTotals[exp.category] || 0) + exp.amount;
    });

    const labels = Object.keys(categoryTotals);
    const data = Object.values(categoryTotals);

    return NextResponse.json({ labels, data });
}