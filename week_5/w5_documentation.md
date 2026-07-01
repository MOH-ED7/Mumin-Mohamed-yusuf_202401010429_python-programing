# Week 5 Lab Tutorial: Cafe Receipt Generator

## Program Description
This Python program simulates a basic point-of-sale receipt generator for a cafe. It prompts the user to input quantities for Coffee, Tea, and Sandwiches, calculates the total bill based on fixed prices, and outputs a formatted receipt.

The project is modularized into two files:
*   `main.py`: Handles user inputs and runs the execution flow.
*   `utils.py`: Contains helper functions for core math calculations and receipt formatting.

---

## Price List Reference

| Item | Price (RM) |
| :--- | :--- |
| Coffee | 8.50 |
| Tea | 6.00 |
| Sandwich | 12.00 |

---

## Functions Implemented

### 1. `calculate_total(coffee, tea, sandwich)`
*   **Purpose**: Multiplies each item's quantity by its respective price and returns the sum.
*   **Formula Used**: `(coffee * 8.50) + (tea * 6.00) + (sandwich * 12.00)`

### 2. `print_receipt(customer_name, coffee, tea, sandwich, total)`
*   **Purpose**: Receives all order metrics and outputs a clean, aligned summary text block acting as a customer receipt.

---

## Test Execution & Sample Output

When executed via the terminal command `python week_5/main.py`, the program successfully prompts and generates the final totals:

```text
Customer name: Ali
Coffee quantity: 3
Tea quantity: 1
Sandwich quantity: 4

===== RECEIPT =====
Customer : Ali
Coffee   : 3
Tea      : 1
Sandwich : 4
-------------------
Total = RM 79.50