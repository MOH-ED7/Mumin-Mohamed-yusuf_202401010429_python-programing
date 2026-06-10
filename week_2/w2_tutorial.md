# Week 2 Tutorial: Movie Theater Admission Logic

### 1. Identify the Components
* **1.1. Inputs:** * Age (Integer)
  * Accompanied by an adult (Boolean: True/False)
  * Has a valid ticket (Boolean: True/False)
* **1.2. Process:** Check if the person is at least 13 OR accompanied by an adult, AND also ensure they have a valid ticket.
* **1.3. Output:** "Access Allowed" or "Access Denied"

### 2. Design the Algorithm
* **2.2. Truth Table:** Let A = Age >= 13, B = Accompanied, C = Has Ticket

| Age >= 13 (A) | Accompanied (B) | Has Ticket (C) | Output (Allowed?) |
| :--- | :--- | :--- | :--- |
| False | False | False | False |
| False | False | True | False |
| False | True | False | False |
| False | True | True | True |
| True | False | False | False |
| True | False | True | True |
| True | True | False | False |
| True | True | True | True |

* **2.3. Step-by-Step Solution:**
  1. Ask for user's age.
  2. Ask if accompanied by an adult.
  3. Ask if they have a ticket.
  4. Evaluate rules: (Age >= 13 OR Accompanied) AND Ticket == True.
  5. Print result.

* **2.4. Pseudocode:**
```text
IF (age >= 13 OR is_accompanied == True) AND has_ticket == True THEN
    OUTPUT "Access Allowed"
ELSE
    OUTPUT "Access Denied"
ENDIF