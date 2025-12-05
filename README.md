# Personal Finance Tracker

A simple and intuitive Python-based personal finance tool to track expenses, save monthly data, and generate insightful reports.

## Features

1. **Add Expenses** - Record expenses with amount, category, description, and date
2. **Save Monthly Expenses** - Export expenses for a specific month to a separate file
3. **Create Reports and Trends** - Generate comprehensive summary and trend reports
4. **Local Storage** - All data is stored locally in JSON format for privacy and easy access

## Installation

No external dependencies required! This tool uses only Python standard library.

### Requirements
- Python 3.6 or higher

## Usage

### Running the Application

```bash
python finance_tracker.py
```

### Main Menu Options

1. **Add Expense** - Enter a new expense with details
   - Amount (e.g., 25.50)
   - Category (e.g., Food, Transport, Entertainment, Utilities)
   - Description (e.g., "Lunch at cafe")
   - Date (optional, defaults to today)

2. **View All Expenses** - Display a list of all recorded expenses

3. **Generate Summary Report** - View overall statistics including:
   - Total expenses
   - Number of transactions
   - Average transaction amount
   - Breakdown by category with percentages

4. **Generate Trends Report** - View monthly trends showing:
   - Monthly totals
   - Top spending categories per month
   - Spending patterns over time

5. **Save Monthly Expenses** - Export expenses for a specific month to a separate JSON file
   - Specify year and month
   - Creates a file like `expenses_2024_12.json`

6. **Exit** - Close the application

## Data Storage

All expenses are automatically saved to `expenses.json` in the same directory as the script.

Monthly exports are saved as `expenses_YYYY_MM.json` files.

### Data Format

```json
[
  {
    "amount": 50.00,
    "category": "Food",
    "description": "Grocery shopping",
    "date": "2024-12-05"
  }
]
```

## Example Workflow

1. Start the application
2. Add several expenses (Option 1)
3. View all expenses to verify (Option 2)
4. Generate a summary report to see spending by category (Option 3)
5. Generate trends report to see monthly patterns (Option 4)
6. Save monthly expenses for archiving (Option 5)

## Tips

- Use consistent category names for better reporting (e.g., always use "Food" instead of mixing "Food", "Groceries", "Dining")
- Review trends regularly to identify spending patterns
- Export monthly data for record-keeping and tax purposes

## License

This project is open source and available for personal use.
