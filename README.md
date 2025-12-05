```bash
Prompt:

Build a small personal finance app called "Expense Tracker with Budget Insights".
Requirements:

Users can add, edit, delete, and fetch expenses via an /expenses REST API.
Each expense has a category, amount, date, and description.
Store all expenses in a database (choose SQLite or PostgreSQL for ease of use).
Provide a monthly chart that summarizes category-wise spending; use a simple web frontend (React or plain HTML/JS) to visualize this.
Integrate an AI-powered insights feature:
Analyze spending trends and suggest budget improvements.
Highlight unusual expenses or spending anomalies.
Make the app simple and easy to run locally.
Organize the code with clear separation of backend (API, database) and frontend (charts, insights).
Please scaffold the project, including backend API, database models, and a basic frontend with charting. Add example code for budget analysis (trends/anomalies) using a simple ML or heuristic approach.

```

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
