# MySQL Database Operations with Jupyter Notebook

## Overview
This project demonstrates fundamental SQL database operations using a Jupyter Notebook. The notebook creates two relational database tables and performs various SQL queries including WHERE conditions (AND, OR, NOT), ORDER BY, and LIKE operations.

## Project Structure
```
week2/
├── week_assign.ipynb       # Main Jupyter Notebook with SQL operations
└── README.md               # This file
```

## Database Tables

### 1. Department Table
Stores information about company departments.

| Column | Type | Description |
|--------|------|-------------|
| dept_id | INT | Primary key, unique department identifier |
| dept_name | VARCHAR(50) | Name of the department |
| location | VARCHAR(50) | Geographic location of the department |
| budget | INT | Department budget in dollars |

**Sample Data:**
- IT, New York, $500,000
- HR, Boston, $250,000
- Sales, New York, $400,000
- Marketing, Chicago, $300,000

### 2. Employee Table
Stores information about employees and their department assignments.

| Column | Type | Description |
|--------|------|-------------|
| emp_id | INT | Primary key, unique employee identifier |
| emp_name | VARCHAR(50) | Full name of the employee |
| dept_id | INT | Foreign key reference to Department table |
| salary | INT | Employee salary in dollars |
| hire_date | TEXT | Date employee was hired (YYYY-MM-DD) |

**Sample Data:** 6 employees across different departments with varying salaries

## SQL Operations Demonstrated

### 1. WHERE with AND
**Query:** Find employees in IT department with salary > $80,000
```sql
SELECT * FROM Employee 
WHERE dept_id = 1 AND salary > 80000
```
**Expected Result:** Sarah Johnson (emp_id: 102)

### 2. WHERE with OR
**Query:** Find employees in IT or Sales departments
```sql
SELECT * FROM Employee 
WHERE dept_id = 1 OR dept_id = 3
```
**Expected Results:** Employees from IT and Sales departments

### 3. WHERE with NOT
**Query:** Find employees NOT in Marketing department
```sql
SELECT * FROM Employee 
WHERE NOT dept_id = 4
```
**Expected Results:** All employees except those in Marketing

### 4. ORDER BY
**Query:** Sort all employees by salary in descending order
```sql
SELECT * FROM Employee 
ORDER BY salary DESC
```
**Expected Results:** Employees listed from highest to lowest salary

### 5. LIKE
**Query:** Find employees whose names start with 'J'
```sql
SELECT * FROM Employee 
WHERE emp_name LIKE 'J%'
```
**Expected Results:** John Smith, Jennifer Anderson, James Wilson, Jessica Brown

## Requirements

- Python 3.7 or higher
- Jupyter Notebook
- sqlite3 (included with Python)

## Installation & Setup

1. **Ensure Python is installed:**
   ```bash
   python --version
   ```

2. **Install Jupyter Notebook (if not already installed):**
   ```bash
   pip install jupyter
   ```

3. **Navigate to the project directory:**
   ```bash
   cd c:\Users\br04a\Downloads\NeoZeno\week2
   ```

## How to Run

### Option 1: VS Code
1. Open `week_assign.ipynb` in VS Code
2. Install the Jupyter extension if prompted
3. Click "Run All" or run each cell sequentially by clicking the play button

### Option 2: Jupyter Lab/Notebook
1. Open terminal in the project directory
2. Run: `jupyter notebook`
3. Open `week_assign.ipynb` in the browser
4. Run cells from top to bottom (Shift + Enter to run a cell)

## Cell-by-Cell Breakdown

| Cell # | Type | Description |
|--------|------|-------------|
| 1 | Code | Import sqlite3 and establish database connection |
| 2 | Markdown | Project title and overview |
| 3 | Markdown | Department table creation heading |
| 4 | Code | CREATE TABLE Department |
| 5 | Markdown | Employee table creation heading |
| 6 | Code | CREATE TABLE Employee |
| 7 | Markdown | Insert Department data heading |
| 8 | Code | INSERT INTO Department (4 records) |
| 9 | Markdown | Insert Employee data heading |
| 10 | Code | INSERT INTO Employee (6 records) |
| 11 | Markdown | Query 1 heading (WHERE with AND) |
| 12 | Code | Execute AND query |
| 13 | Markdown | Query 2 heading (WHERE with OR) |
| 14 | Code | Execute OR query |
| 15 | Markdown | Query 3 heading (WHERE with NOT) |
| 16 | Code | Execute NOT query |
| 17 | Markdown | Query 4 heading (ORDER BY) |
| 18 | Code | Execute ORDER BY query |
| 19 | Markdown | Query 5 heading (LIKE) |
| 20 | Code | Execute LIKE query |
| 21 | Markdown | Close connection heading |
| 22 | Code | Close database connection |

## Key Concepts Covered

### SQL Operators
- **AND:** Combine multiple conditions (both must be true)
- **OR:** Multiple conditions (at least one must be true)
- **NOT:** Negate a condition
- **LIKE:** Pattern matching with wildcards (% = any characters, _ = single character)
- **ORDER BY:** Sort results by specified column(s)

### Database Operations
- **CREATE TABLE:** Define table structure
- **INSERT INTO:** Add records to a table
- **SELECT:** Retrieve data from tables
- **DROP TABLE:** Remove existing tables (if present)

## Database Technology
- **SQLite3:** Lightweight, file-less database engine
- No server configuration required
- Ideal for learning and development
- Easily portable across platforms

## Expected Output
When all cells are executed successfully, you should see:
1. "Successfully connected to SQLite database"
2. "Department table created successfully"
3. "Employee table created successfully"
4. "Inserted 4 records into Department table"
5. "Inserted 6 records into Employee table"
6. Query results showing employee records matching each condition

## Troubleshooting

**Issue:** Kernel error or connection failure
- Solution: Restart the kernel and run cells in order from the top

**Issue:** Table doesn't exist error
- Solution: Ensure table creation cells (cells 4 and 6) executed successfully

**Issue:** No results from queries
- Solution: Verify data insertion cells executed and returned "Inserted X records"

## Learning Outcomes
After completing this notebook, you will understand:
- How to create database tables with proper structure
- How to insert sample data into tables
- How to write SQL WHERE clauses with multiple conditions
- How to sort query results using ORDER BY
- How to use pattern matching with LIKE
- Basic relational database concepts

## Additional Resources
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [SQL Tutorial](https://www.w3schools.com/sql/)
- [Jupyter Notebook Guide](https://jupyter-notebook.readthedocs.io/)

## Author
Week 2 Assignment - NeoZeno Bootcamp

## License
This project is for educational purposes.

---

**Last Updated:** February 9, 2026
