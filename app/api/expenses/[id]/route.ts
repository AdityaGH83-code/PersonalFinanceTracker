import { NextRequest, NextResponse } from 'next/server';
import db from '../../../../lib/db';

export async function GET(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
    const { id } = await params;
    const expense = db.prepare('SELECT * FROM expenses WHERE id = ?').get(id);
    if (!expense) {
        return NextResponse.json({ error: 'Expense not found' }, { status: 404 });
    }
    return NextResponse.json(expense);
}

export async function PUT(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
    const { id } = await params;
    const body = await request.json();
    const { category, amount, date, description } = body;
    const stmt = db.prepare('UPDATE expenses SET category = ?, amount = ?, date = ?, description = ? WHERE id = ?');
    const result = stmt.run(category, amount, date, description, id);
    if (result.changes === 0) {
        return NextResponse.json({ error: 'Expense not found' }, { status: 404 });
    }
    return NextResponse.json({ message: 'Updated' });
}

export async function DELETE(request: NextRequest, { params }: { params: Promise<{ id: string }> }) {
    const { id } = await params;
    const stmt = db.prepare('DELETE FROM expenses WHERE id = ?');
    const result = stmt.run(id);
    if (result.changes === 0) {
        return NextResponse.json({ error: 'Expense not found' }, { status: 404 });
    }
    return NextResponse.json({ message: 'Deleted' });
}