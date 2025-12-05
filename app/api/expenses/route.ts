import { NextRequest, NextResponse } from 'next/server';
import db from '../../../lib/db';

export async function GET() {
  const expenses = db.prepare('SELECT * FROM expenses').all();
  return NextResponse.json(expenses);
}

export async function POST(request: NextRequest) {
  const body = await request.json();
  const { category, amount, date, description } = body;
  const stmt = db.prepare('INSERT INTO expenses (category, amount, date, description) VALUES (?, ?, ?, ?)');
  const result = stmt.run(category, amount, date, description);
  return NextResponse.json({ id: result.lastInsertRowid });
}