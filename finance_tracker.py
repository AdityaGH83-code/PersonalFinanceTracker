#!/usr/bin/env python3
"""
Personal Finance Tracker
A simple tool to track expenses, save monthly data, and generate reports.
"""

import json
import os
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Optional


class Expense:
    """Represents a single expense entry."""
    
    def __init__(self, amount: float, category: str, description: str, date: str = None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime("%Y-%m-%d")
    
    def to_dict(self) -> Dict:
        """Convert expense to dictionary."""
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Expense':
        """Create expense from dictionary."""
        return cls(
            amount=data['amount'],
            category=data['category'],
            description=data['description'],
            date=data['date']
        )
    
    def __str__(self) -> str:
        return f"{self.date} | {self.category:15} | ${self.amount:8.2f} | {self.description}"


class StorageManager:
    """Manages local storage of expenses data."""
    
    def __init__(self, filename: str = "expenses.json"):
        self.filename = filename
    
    def save_expenses(self, expenses: List[Expense]) -> None:
        """Save expenses to local storage."""
        data = [expense.to_dict() for expense in expenses]
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_expenses(self) -> List[Expense]:
        """Load expenses from local storage."""
        if not os.path.exists(self.filename):
            return []
        
        with open(self.filename, 'r') as f:
            data = json.load(f)
        
        return [Expense.from_dict(item) for item in data]


class FinanceTracker:
    """Main finance tracker application."""
    
    def __init__(self, storage_file: str = "expenses.json"):
        self.storage = StorageManager(storage_file)
        self.expenses = self.storage.load_expenses()
    
    def add_expense(self, amount: float, category: str, description: str, date: str = None) -> None:
        """Add a new expense."""
        expense = Expense(amount, category, description, date)
        self.expenses.append(expense)
        self.storage.save_expenses(self.expenses)
        print(f"✓ Expense added: ${amount:.2f} for {category}")
    
    def get_monthly_expenses(self, year: int, month: int) -> List[Expense]:
        """Get all expenses for a specific month."""
        month_str = f"{year}-{month:02d}"
        return [exp for exp in self.expenses if exp.date.startswith(month_str)]
    
    def save_monthly_report(self, year: int, month: int) -> None:
        """Save monthly expenses to a separate file."""
        monthly_expenses = self.get_monthly_expenses(year, month)
        filename = f"expenses_{year}_{month:02d}.json"
        
        data = [expense.to_dict() for expense in monthly_expenses]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        total = sum(exp.amount for exp in monthly_expenses)
        print(f"✓ Monthly report saved to {filename}")
        print(f"  Total expenses: ${total:.2f} ({len(monthly_expenses)} transactions)")
    
    def generate_summary_report(self) -> None:
        """Generate and display a summary report of all expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n" + "="*70)
        print("EXPENSE SUMMARY REPORT".center(70))
        print("="*70)
        
        # Overall statistics
        total = sum(exp.amount for exp in self.expenses)
        avg = total / len(self.expenses)
        
        print(f"\nTotal Expenses: ${total:.2f}")
        print(f"Number of Transactions: {len(self.expenses)}")
        print(f"Average Transaction: ${avg:.2f}")
        
        # Category breakdown
        print("\n" + "-"*70)
        print("EXPENSES BY CATEGORY")
        print("-"*70)
        
        category_totals = defaultdict(float)
        category_counts = defaultdict(int)
        
        for exp in self.expenses:
            category_totals[exp.category] += exp.amount
            category_counts[exp.category] += 1
        
        sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
        
        for category, amount in sorted_categories:
            percentage = (amount / total) * 100
            count = category_counts[category]
            print(f"{category:20} ${amount:10.2f} ({percentage:5.1f}%) - {count} transactions")
        
        print("="*70 + "\n")
    
    def generate_trends_report(self) -> None:
        """Generate and display trends report (monthly breakdown)."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n" + "="*70)
        print("MONTHLY TRENDS REPORT".center(70))
        print("="*70)
        
        # Group by month
        monthly_totals = defaultdict(float)
        monthly_counts = defaultdict(int)
        monthly_categories = defaultdict(lambda: defaultdict(float))
        
        for exp in self.expenses:
            month_key = exp.date[:7]  # YYYY-MM
            monthly_totals[month_key] += exp.amount
            monthly_counts[month_key] += 1
            monthly_categories[month_key][exp.category] += exp.amount
        
        sorted_months = sorted(monthly_totals.keys())
        
        for month in sorted_months:
            total = monthly_totals[month]
            count = monthly_counts[month]
            
            print(f"\n{month} - Total: ${total:.2f} ({count} transactions)")
            print("  Top categories:")
            
            top_categories = sorted(
                monthly_categories[month].items(),
                key=lambda x: x[1],
                reverse=True
            )[:3]
            
            for category, amount in top_categories:
                percentage = (amount / total) * 100
                print(f"    • {category:15} ${amount:8.2f} ({percentage:5.1f}%)")
        
        print("\n" + "="*70 + "\n")
    
    def list_all_expenses(self) -> None:
        """List all expenses."""
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print("\n" + "="*70)
        print("ALL EXPENSES".center(70))
        print("="*70)
        print(f"{'Date':<12} | {'Category':<15} | {'Amount':>10} | Description")
        print("-"*70)
        
        for exp in sorted(self.expenses, key=lambda x: x.date, reverse=True):
            print(exp)
        
        print("="*70 + "\n")


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("PERSONAL FINANCE TRACKER".center(50))
    print("="*50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Generate Summary Report")
    print("4. Generate Trends Report")
    print("5. Save Monthly Expenses")
    print("6. Exit")
    print("="*50)


def main():
    """Main application loop."""
    tracker = FinanceTracker()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            # Add expense
            try:
                amount = float(input("Enter amount: $"))
                if amount <= 0:
                    print("✗ Amount must be greater than zero.")
                    continue
                
                category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
                if not category:
                    print("✗ Category cannot be empty.")
                    continue
                
                description = input("Enter description: ").strip()
                if not description:
                    print("✗ Description cannot be empty.")
                    continue
                
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
                
                # Validate date format if provided
                date = None
                if date_input:
                    try:
                        datetime.strptime(date_input, "%Y-%m-%d")
                        date = date_input
                    except ValueError:
                        print("✗ Invalid date format. Please use YYYY-MM-DD format.")
                        continue
                
                tracker.add_expense(amount, category, description, date)
            except ValueError:
                print("✗ Invalid amount. Please enter a valid number.")
            except Exception as e:
                print(f"✗ Error: {e}")
        
        elif choice == '2':
            # View all expenses
            tracker.list_all_expenses()
        
        elif choice == '3':
            # Generate summary report
            tracker.generate_summary_report()
        
        elif choice == '4':
            # Generate trends report
            tracker.generate_trends_report()
        
        elif choice == '5':
            # Save monthly expenses
            try:
                year = int(input("Enter year (e.g., 2024): "))
                if year < 1900 or year > 2100:
                    print("✗ Please enter a reasonable year between 1900 and 2100.")
                    continue
                
                month = int(input("Enter month (1-12): "))
                if month < 1 or month > 12:
                    print("✗ Month must be between 1 and 12.")
                    continue
                
                tracker.save_monthly_report(year, month)
            except ValueError:
                print("✗ Invalid year or month.")
            except Exception as e:
                print(f"✗ Error: {e}")
        
        elif choice == '6':
            # Exit
            print("\nThank you for using Personal Finance Tracker!")
            break
        
        else:
            print("✗ Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
