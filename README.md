# InventoryW2M1

## Overview

This project is a console-based inventory management system built with Python.
It allows users to manage products using basic operations such as adding, searching, updating, and deleting.

The system uses lists and dictionaries to store data in memory.

---

## Features

* Add products to inventory
* Show all products
* Search products by name
* Update product information
* Delete products
* Input validation
* Error handling

---

## Data Structure

The inventory is stored as a list of dictionaries:

```python
{
    "name": str,
    "price": float,
    "quantity": int
}
```

---

## How It Works

The program runs in a loop and displays a menu with options from 1 to 6.
The user selects an option and the system executes the corresponding function.

---

## Menu Options

1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. Exit

---

## Validation

* Price must be a number and not negative
* Quantity must be an integer and not negative
* Invalid inputs are handled using try/except

---

## Error Handling

The system prevents crashes by handling:

* Invalid numeric input
* Incorrect menu options
* Missing products

---

## How to Run

Run the program using:

```bash
python inventory_app.py
```

---

## Requirements Covered

* Lists and dictionaries
* Functions
* CRUD operations
* Input validation
* Basic error handling

---

## Notes

* Data is stored only in memory (not saved to files)
* The program runs entirely in the console

---

## Conclusion

This project demonstrates the use of Python fundamentals to build a functional inventory system with clean structure and user interaction.

---

## FlowChart

<img width="1340" height="1071" alt="image" src="https://github.com/user-attachments/assets/31f57ccd-2c9c-43ab-93b2-598dc46a9d45" />

