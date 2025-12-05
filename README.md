# Expense Tracker with Budget Insights

A simple personal finance app built with Next.js, featuring expense tracking, budget insights, and data visualization.

## Features

- Add, edit, delete, and view expenses via REST API
- Monthly category-wise spending chart
- AI-powered insights: spending trends, anomaly detection, budget suggestions
- SQLite database for easy local setup

## Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```

2. Run the development server:
   ```bash
   npm run dev
   ```

3. Open [http://localhost:3000](http://localhost:3000) in your browser.

## API Endpoints

- `GET /api/expenses` - Fetch all expenses
- `POST /api/expenses` - Add a new expense
- `GET /api/expenses/[id]` - Fetch a specific expense
- `PUT /api/expenses/[id]` - Update an expense
- `DELETE /api/expenses/[id]` - Delete an expense
- `GET /api/chart` - Get monthly spending data for chart
- `GET /api/insights` - Get budget insights and anomalies

## Technologies Used

- Next.js (App Router)
- TypeScript
- Tailwind CSS
- better-sqlite3 (SQLite database)
- Chart.js (data visualization)
