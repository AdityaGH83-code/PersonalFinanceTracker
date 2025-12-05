#!/usr/bin/env python3
"""
Demo script to test all features of the Personal Finance Tracker
"""

from finance_tracker import FinanceTracker

def demo():
    print("="*70)
    print("PERSONAL FINANCE TRACKER - DEMO")
    print("="*70)
    
    # Initialize tracker
    tracker = FinanceTracker("demo_expenses.json")
    
    # 1. Add expenses
    print("\n1. ADDING EXPENSES")
    print("-"*70)
    tracker.add_expense(50.00, "Food", "Grocery shopping", "2024-11-15")
    tracker.add_expense(25.50, "Transport", "Taxi ride", "2024-11-20")
    tracker.add_expense(75.00, "Entertainment", "Movie tickets", "2024-11-25")
    tracker.add_expense(120.00, "Food", "Restaurant dinner", "2024-12-01")
    tracker.add_expense(30.00, "Utilities", "Internet bill", "2024-12-02")
    tracker.add_expense(45.00, "Transport", "Bus pass", "2024-12-03")
    tracker.add_expense(200.00, "Shopping", "New shoes", "2024-12-04")
    tracker.add_expense(15.00, "Food", "Coffee shop", "2024-12-05")
    
    # 2. View all expenses
    print("\n2. VIEWING ALL EXPENSES")
    print("-"*70)
    tracker.list_all_expenses()
    
    # 3. Generate summary report
    print("\n3. SUMMARY REPORT")
    print("-"*70)
    tracker.generate_summary_report()
    
    # 4. Generate trends report
    print("\n4. TRENDS REPORT")
    print("-"*70)
    tracker.generate_trends_report()
    
    # 5. Save monthly expenses
    print("\n5. SAVING MONTHLY EXPENSES")
    print("-"*70)
    tracker.save_monthly_report(2024, 11)
    tracker.save_monthly_report(2024, 12)
    
    print("\n" + "="*70)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("="*70)
    print("\nGenerated files:")
    print("  - demo_expenses.json (all expenses)")
    print("  - expenses_2024_11.json (November 2024 expenses)")
    print("  - expenses_2024_12.json (December 2024 expenses)")

if __name__ == "__main__":
    demo()
