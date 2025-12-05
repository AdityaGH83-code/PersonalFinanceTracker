# Personal Finance Tracker - Quick Start Guide

## Installation
No installation needed! Just make sure you have Python 3.6+ installed.

## Running the Application

```bash
python finance_tracker.py
```

## Quick Example

Here's a quick walkthrough of using all features:

### 1. Add an Expense
```
Enter your choice (1-6): 1
Enter amount: $50.00
Enter category (e.g., Food, Transport, Entertainment): Food
Enter description: Grocery shopping
Enter date (YYYY-MM-DD) or press Enter for today: [Press Enter]
✓ Expense added: $50.00 for Food
```

### 2. Add More Expenses
Continue adding more expenses:
- $25.50 for Transport (Taxi ride)
- $75.00 for Entertainment (Movie tickets)
- $120.00 for Food (Restaurant dinner)

### 3. View All Expenses
```
Enter your choice (1-6): 2
```

This displays all your expenses in a formatted table.

### 4. Generate Summary Report
```
Enter your choice (1-6): 3
```

Shows:
- Total expenses
- Number of transactions
- Average transaction amount
- Breakdown by category with percentages

### 5. Generate Trends Report
```
Enter your choice (1-6): 4
```

Shows:
- Monthly totals
- Top spending categories per month
- Spending patterns over time

### 6. Save Monthly Expenses
```
Enter your choice (1-6): 5
Enter year (e.g., 2024): 2024
Enter month (1-12): 12
✓ Monthly report saved to expenses_2024_12.json
```

Creates a separate file with all expenses for December 2024.

## Running the Demo

To see all features in action with sample data:

```bash
python demo.py
```

This will:
1. Add 8 sample expenses
2. Display all expenses
3. Generate summary report
4. Generate trends report
5. Save monthly reports for November and December 2024

## Data Files

- `expenses.json` - Main storage file (created automatically)
- `expenses_YYYY_MM.json` - Monthly export files

## Tips

1. **Consistent Categories**: Use the same category names (e.g., always "Food" not "food" or "Groceries")
2. **Regular Reviews**: Check your summary and trends reports regularly to understand spending patterns
3. **Monthly Exports**: Save monthly reports for record-keeping and tax purposes
4. **Backup**: Since data is stored locally in JSON files, consider backing them up periodically

## Common Categories

Here are some suggested categories to keep your data organized:
- Food
- Transport
- Entertainment
- Utilities
- Shopping
- Healthcare
- Education
- Housing
- Savings
- Miscellaneous

## Example Workflow

1. **Daily**: Add expenses as they occur
2. **Weekly**: View all expenses to verify entries
3. **Monthly**: Generate reports and save monthly data
4. **Quarterly**: Review trends to identify spending patterns

Enjoy tracking your finances! 📊💰
