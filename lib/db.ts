import Database from 'better-sqlite3';

export interface Expense {
  id?: number;
  category: string;
  amount: number;
  date: string;
  description: string;
}

const db = new Database('expenses.db');

db.exec(`
  CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL,
    description TEXT
  )
`);

export default db;